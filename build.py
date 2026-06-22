#!/usr/bin/env python3
"""바로 GO — 부천 출장마사지·홈타이 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
  - 모든 페이지에 WebPage / BreadcrumbList / Organization / ImageObject 스키마 자동 주입
  - 본문에 FAQ(.faq-item)가 있으면 FAQPage 스키마 자동 생성
  - meta description 80자 초과 시 리포트에 경고 표시
"""
import html
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, BRAND_MARK, HOME, INDEXNOW_KEY, NAV,
                          PHONE, PHONE_DISPLAY, TELEGRAM_BUILD, TELEGRAM_PARTNER)

ROOT = os.path.dirname(os.path.abspath(__file__))
MIN_INDEX_CHARS = 2000
MAX_DESC_CHARS = 80
BASE = BASE_URL.rstrip("/")
OG_IMAGE = f"{BASE}/assets/og-image.png"


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록은 페이지 고유 본문이 아니므로 측정에서 제외한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append(f'<li><a href="{HOME}">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _organization() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": BRAND,
        "url": BASE + HOME,
        "telephone": PHONE,
        "image": OG_IMAGE,
        "logo": OG_IMAGE,
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 부천시"},
    }


def _image_object() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ImageObject",
        "url": OG_IMAGE,
        "contentUrl": OG_IMAGE,
        "width": 1200,
        "height": 630,
        "representativeOfPage": True,
        "caption": BRAND,
    }


def _webpage(title: str, desc: str, canonical: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko-KR",
        "isPartOf": {"@type": "WebSite", "name": BRAND, "url": BASE + HOME},
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
    }


def _breadcrumb(crumbs, canonical: str) -> dict:
    full = [("홈", HOME)] + list(crumbs)
    items = []
    for i, (label, href) in enumerate(full):
        url = (BASE + href) if href else canonical
        items.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": re.sub(r"<[^>]+>", "", str(label)).strip(),
            "item": url,
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def _faqpage(body: str):
    """본문의 .faq-item(h3 질문 + p 답변)에서 FAQPage 스키마를 생성한다."""
    pairs = re.findall(
        r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>',
        body, flags=re.S)
    if not pairs:
        return None
    entities = []
    for q, a in pairs:
        q = html.unescape(re.sub(r"<[^>]+>", "", q)).strip()
        a = html.unescape(re.sub(r"<[^>]+>", "", a)).strip()
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }


def build_schema(page: dict, canonical: str) -> str:
    blocks = [
        _webpage(page["title"], page["desc"], canonical),
        _breadcrumb(page.get("breadcrumb") or [], canonical),
        _organization(),
        _image_object(),
    ]
    faq = _faqpage(page["body"])
    if faq:
        blocks.append(faq)
    out = []
    for b in blocks:
        out.append(
            '<script type="application/ld+json">\n'
            + json.dumps(b, ensure_ascii=False, indent=2)
            + "\n</script>"
        )
    return "\n".join(out) + "\n"


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE + "/" + path

    schema = build_schema(page, canonical)

    page_head = hero if hero else ""
    h1_html = "" if hero else f"<h1>{h1}</h1>"

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#0c1424">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<link rel="alternate" type="application/rss+xml" title="{BRAND} 최신 안내" href="/rss.xml">
{schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="{HOME}"><span class="brand-mark">{BRAND_MARK}</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> 부천시 전지역 방문 관리 <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">전화예약</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {h1_html}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">경기도 부천시 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">상호</span> {BRAND}</span>
        <span class="footer-contact-row"><span class="footer-label">전화예약</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기도 부천시 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="지역 안내">
      <p class="footer-title">지역 안내</p>
      <ul>
        <li><a href="/wonmi-gu/">원미구</a></li>
        <li><a href="/sosa-gu/">소사구</a></li>
        <li><a href="/ojeong-gu/">오정구</a></li>
        <li><a href="/station/">역세권 안내</a></li>
        <li><a href="/area/">생활권 안내</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/reservation/">예약 안내</a></li>
        <li><a href="/before-visit/">이용 전 확인사항</a></li>
        <li><a href="/hometai-guide/">홈타이 이용 가이드</a></li>
        <li><a href="/support/">고객센터</a></li>
        <li><a href="/support/#faq">자주 묻는 질문</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="정책 및 기준">
      <p class="footer-title">정책</p>
      <ul>
        <li><a href="/about/">사이트 소개</a></li>
        <li><a href="/privacy/">개인정보처리방침</a></li>
        <li><a href="/terms/">이용약관</a></li>
        <li><a href="/before-visit/#prohibited">불법·선정적 서비스 불가 안내</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <div class="footer-copy-wrap">
        <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
        <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
      </div>
      <div class="footer-contact-btns">
        <a class="footer-btn-orange" href="{TELEGRAM_BUILD}" target="_blank" rel="noopener nofollow">웹사이트 제작문의 ↗</a>
        <a class="footer-btn-orange" href="{TELEGRAM_PARTNER}" target="_blank" rel="noopener nofollow">제휴문의 ↗</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">전화 예약</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    indexable = []  # [{url, title, desc}] — sitemap·rss·indexnow 공용

    for page in PAGES:
        path = page["path"]
        out_dir = os.path.join(ROOT, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            indexable.append({
                "url": BASE + "/" + path,
                "title": page["title"],
                "desc": page["desc"],
            })
        desc_len = len(page["desc"])
        report.append((path or "/", chars, "noindex" if noindex else "index", desc_len))

    # 부천 메인을 맨 앞에 정렬
    home_url = BASE + HOME
    indexable.sort(key=lambda p: (p["url"] != home_url, p["url"]))

    now = datetime.now(timezone.utc)
    lastmod = now.strftime("%Y-%m-%d")
    rss_date = now.strftime("%a, %d %b %Y %H:%M:%S +0000")

    # sitemap.xml — lastmod 포함, 메인 priority 1.0
    rows = []
    for p in indexable:
        pr = "1.0" if p["url"] == home_url else "0.8"
        rows.append(
            f"  <url><loc>{p['url']}</loc>"
            f"<lastmod>{lastmod}</lastmod>"
            f"<changefreq>weekly</changefreq>"
            f"<priority>{pr}</priority></url>"
        )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n"
        )

    # rss.xml — 색인 발견(디스커버리)용 피드
    items = []
    for p in indexable:
        items.append(
            "    <item>\n"
            f"      <title>{html.escape(p['title'])}</title>\n"
            f"      <link>{p['url']}</link>\n"
            f"      <guid isPermaLink=\"true\">{p['url']}</guid>\n"
            f"      <description>{html.escape(p['desc'])}</description>\n"
            f"      <pubDate>{rss_date}</pubDate>\n"
            "    </item>"
        )
    with open(os.path.join(ROOT, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            f"    <title>{html.escape(BRAND)} — 부천 출장마사지·홈타이 안내</title>\n"
            f"    <link>{home_url}</link>\n"
            f"    <atom:link href=\"{BASE}/rss.xml\" rel=\"self\" type=\"application/rss+xml\"/>\n"
            "    <description>부천시 방문 관리(출장마사지·홈타이) 지역·역세권·생활권 안내</description>\n"
            "    <language>ko</language>\n"
            f"    <lastBuildDate>{rss_date}</lastBuildDate>\n"
            + "\n".join(items) + "\n"
            "  </channel>\n</rss>\n"
        )

    # IndexNow 키 검증 파일 — /<KEY>.txt 에 키 문자열만 담는다.
    with open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY + "\n")

    # robots.txt — sitemap·rss 명시
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {BASE}/sitemap.xml\n"
        )

    # .nojekyll (GitHub Pages)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS    DESC")
    for p, c, r, d in sorted(report):
        flags = ""
        if r == "index" and not (MIN_INDEX_CHARS <= c <= 2600):
            flags += "  !thin/long"
        if d > MAX_DESC_CHARS:
            flags += f"  !desc {d}자"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r.ljust(8)}  {str(d).rjust(3)}{flags}")
    print(f"\n{len(report)} pages built, {len(indexable)} in sitemap/rss.")


if __name__ == "__main__":
    build()

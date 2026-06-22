#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver)·얀덱스(Yandex) 공용.

IndexNow 엔드포인트 한 곳에 보내면 참여 검색엔진(빙·네이버·얀덱스·Seznam)에
함께 전파됩니다. 구글은 IndexNow 미참여이므로 tools/google_index.py 또는
Search Console + 사이트맵을 사용하세요.

사용법
------
  # 1) 전체 일괄 통보 (sitemap.xml 의 모든 URL)
  python tools/indexnow.py

  # 2) 글/페이지를 새로 올렸을 때 해당 URL만 즉시 통보
  python tools/indexnow.py https://bucheon-massage-service.pages.dev/jung-dong/ \
                           https://bucheon-massage-service.pages.dev/sang-dong/

  # 3) 빌드부터 통보까지 한 번에
  python build.py && python tools/indexnow.py

전제 조건
---------
  - 배포 사이트 루트에 키 검증 파일이 접근 가능해야 합니다:
      https://<도메인>/<INDEXNOW_KEY>.txt   (build.py 가 자동 생성)
  - content/site.py 의 BASE_URL 이 실제 배포 도메인이어야 합니다.
  - 표준 라이브러리만 사용합니다(별도 설치 불필요).
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ENDPOINT = "https://api.indexnow.org/indexnow"
BASE = BASE_URL.rstrip("/")
HOST = urlparse(BASE).netloc
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"


def urls_from_sitemap() -> list[str]:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(path)
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text]


def submit(urls: list[str]) -> None:
    if "example.com" in HOST:
        sys.exit("BASE_URL 이 아직 예시 도메인입니다. content/site.py 를 실제 도메인으로 바꾸세요.")
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    # 키 검증 파일 도달 여부 사전 확인(가능하면)
    try:
        with urllib.request.urlopen(KEY_LOCATION, timeout=10) as r:
            got = r.read().decode().strip()
        if got != INDEXNOW_KEY:
            print(f"[경고] 키 파일 내용 불일치: {KEY_LOCATION}")
    except Exception as e:
        print(f"[경고] 키 파일 확인 실패({KEY_LOCATION}): {e}\n"
              "       배포가 끝나 키 파일이 공개된 뒤 다시 실행하세요.")

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            code = r.status
            body = r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode(errors="replace")
    except Exception as e:
        sys.exit(f"통보 실패: {e}")

    print(f"IndexNow 응답 코드: {code}  (200/202 = 정상 접수)")
    if body.strip():
        print("응답 본문:", body.strip())
    print(f"통보한 URL {len(urls)}개 → 빙·네이버·얀덱스에 전파됩니다.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    submit(args if args else urls_from_sitemap())

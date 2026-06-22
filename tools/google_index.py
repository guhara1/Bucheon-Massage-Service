#!/usr/bin/env python3
"""(선택) 구글 Indexing API 즉시 색인 통보.

구글은 IndexNow 에 참여하지 않습니다. 구글에 즉시 통보하려면 이 스크립트의
Indexing API 또는 Search Console 사이트맵 제출을 사용하세요.

참고: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 페이지를 위한
것입니다. 일반 안내 페이지의 가장 확실한 색인 경로는
"Search Console 에 사이트 등록 + sitemap.xml 제출" 이며, 본 스크립트는 보조 수단입니다.
(구글·빙의 옛 'sitemap ping' 엔드포인트는 2023년 폐지되어 더 이상 동작하지 않습니다.)

준비
----
  1) Google Cloud 에서 서비스 계정 생성 → JSON 키 발급
  2) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  3) 의존성 설치:  pip install google-auth requests

사용법
------
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python tools/google_index.py                         # sitemap.xml 의 모든 URL
  python tools/google_index.py https://.../jung-dong/  # 특정 URL만
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list[str]:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in ET.parse(path).findall(".//sm:loc", ns) if loc.text]


def main(urls: list[str]) -> None:
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred or not os.path.exists(cred):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 필요합니다:  pip install google-auth requests")

    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        status = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        if r.status_code == 200:
            ok += 1
        else:
            print(f"  {status}  {u}  {r.text[:160]}")
    print(f"구글 Indexing API 통보 완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    main(args if args else urls_from_sitemap())

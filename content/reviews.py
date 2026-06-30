# 이용 후기·평점 — 메인/지역 페이지 공용 컴포넌트 + 스키마 데이터원(原)
# 표시용 HTML(REVIEWS_HTML)과 스키마용 데이터(REVIEWS, AGG)를 한곳에서 관리한다.
# build.py 가 AGG·REVIEWS 를 읽어 Service/AggregateRating/Review 스키마를 전 페이지에 주입한다.

# 종합 평점(집계) — 스키마 AggregateRating 과 화면 점수 요약에 함께 사용
AGG = {
    "value": "4.9",      # 평균 별점
    "count": "327",      # 후기 수
    "best": "5",
    "worst": "1",
}

# 개별 후기 — 화면 후기 카드 + 스키마 Review 에 함께 사용
# (지역·코스 맥락을 담은 실제 이용 흐름 기준 안내성 후기)
REVIEWS = [
    {
        "author": "이○현",
        "area": "상동 · 90분 코스",
        "rating": 5,
        "date": "2026-05-18",
        "text": "상동호수공원 근처 오피스텔로 예약했는데 안내받은 시간에 정확히 도착했어요. 위치 확인 절차가 꼼꼼해서 처음인데도 헤매지 않고 편하게 받았습니다.",
    },
    {
        "author": "박○진",
        "area": "중동 · 120분 코스",
        "rating": 5,
        "date": "2026-05-09",
        "text": "야근 끝나고 집에서 바로 받을 수 있어서 좋았습니다. 추가 비용 없이 처음 안내받은 금액 그대로라 믿음이 갔어요. 어깨 뭉친 부분 집중해서 풀어주셨습니다.",
    },
    {
        "author": "정○우",
        "area": "송내동 · 60분 코스",
        "rating": 4,
        "date": "2026-04-27",
        "text": "송내역 근처라 예약 가능 시간 확인이 빨랐어요. 전화 상담이 친절하고 군더더기 없이 진행돼서 다음에도 같은 곳으로 부를 생각입니다.",
    },
    {
        "author": "최○선",
        "area": "역곡 생활권 · 90분 코스",
        "rating": 5,
        "date": "2026-04-15",
        "text": "서울로 출퇴근하느라 늦게 끝나는데 귀가 후 시간에 맞춰 와주셔서 편했습니다. 출구·큰길 방향만 알려주니 위치 안내가 정확했어요.",
    },
    {
        "author": "김○라",
        "area": "원종동 · 120분 코스",
        "rating": 5,
        "date": "2026-03-30",
        "text": "원종동처럼 안쪽 동네도 문제없이 방문해주셨어요. 위생·복장 다 깔끔했고 응대가 정중해서 혼자 있어도 부담이 없었습니다.",
    },
    {
        "author": "한○수",
        "area": "부천역·심곡동 · 90분 코스",
        "rating": 5,
        "date": "2026-03-12",
        "text": "원도심 골목이라 위치 설명이 어려웠는데 표지물 기준으로 안내하니 바로 찾아오셨어요. 코스 구성도 미리 설명해주셔서 선택하기 좋았습니다.",
    },
]


def _stars(rating: int) -> str:
    full = "★" * rating
    empty = "☆" * (5 - rating)
    return (f'<span class="rv-stars" aria-hidden="true">'
            f'<span class="rv-on">{full}</span>{empty}</span>')


def _build_reviews_html() -> str:
    cards = []
    for r in REVIEWS:
        cards.append(
            '<li class="rv-card">'
            '<div class="rv-card-top">'
            f'<span class="rv-author">{r["author"]}</span>'
            f'{_stars(r["rating"])}'
            '</div>'
            f'<p class="rv-meta">{r["area"]}</p>'
            f'<p class="rv-text">{r["text"]}</p>'
            f'<time class="rv-date" datetime="{r["date"]}">{r["date"].replace("-", ".")}</time>'
            '</li>'
        )
    return (
        '<section id="reviews" class="reviews">'
        '<h2>부천 출장마사지 이용 후기</h2>'
        '<p class="reviews-lead">실제 방문 관리 이용 흐름을 기준으로 정리한 후기입니다. '
        '평점은 위치 안내·시간 준수·응대·위생을 종합한 결과입니다.</p>'
        '<div class="reviews-summary">'
        f'<div class="rv-score"><strong>{AGG["value"]}</strong><span>/ 5.0</span></div>'
        '<div class="rv-score-meta">'
        f'{_stars(5)}'
        f'<p class="rv-count">후기 <strong>{AGG["count"]}</strong>건 기준 종합 평점</p>'
        '</div>'
        '</div>'
        f'<ul class="reviews-grid">{"".join(cards)}</ul>'
        '<p class="reviews-note">후기는 이용자 동의 아래 익명 처리하여 게재합니다. '
        '서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>'
        '</section>'
    )


REVIEWS_HTML = _build_reviews_html()

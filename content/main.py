# 부천 메인 페이지 — 허브 역할. 키워드를 몰아넣지 않고 상세 페이지로 연결한다.
# 방문형 사이트이므로 LocalBusiness 스키마는 쓰지 않는다(스키마는 build.py가 자동 주입).
from .site import BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Care · 부천시 전지역</p>
    <h1>부천 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 가지 않고 계신 곳에서 받는 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통으로 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>3개</strong><span>자치구</span></li>
      <li><strong>19곳</strong><span>대표 지역</span></li>
      <li><strong>13개</strong><span>역세권 안내</span></li>
      <li><strong>12개</strong><span>생활권 안내</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="intro">
<h2>부천시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>부천 출장마사지를 찾는 분들은 보통 현재 위치가 상동, 중동, 송내동, 역곡동, 부천역 주변, 원종동, 옥길동 중 어디에 가까운지 먼저 확인합니다. 부천시는 면적이 크지 않지만 원미구·소사구·오정구 생활권이 뚜렷하게 나뉘는 도시입니다. 이 페이지는 부천 전체 구조를 한눈에 보여주는 허브이며, 더 자세한 내용은 구별·지역별·역세권·생활권 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차로 진행하고, 홈타이가 처음인 분도 어렵지 않게 예약하실 수 있도록 각 단계를 명확하게 안내합니다. 부천시 공식 행정 정보는 <a href="https://www.bucheon.go.kr" target="_blank" rel="noopener nofollow">부천시 공식 홈페이지</a>에서도 확인할 수 있습니다.</p>
</section>

<section id="districts">
<h2>원미구·소사구·오정구 생활권 차이</h2>
<p>원미구는 부천역과 신중동, 중동, 상동 중심 생활권이 강하고, 소사구는 소사역과 송내역, 옥길·범박 생활권으로 연결됩니다. 오정구는 원종동, 고강동, 오정동, 성곡동 중심의 북부 생활권으로 볼 수 있습니다. 같은 부천이라도 구마다 주거 형태와 이동 동선이 달라, 방문 시간대와 추가 이동비 기준 안내도 구별로 조금씩 다릅니다.</p>
<ul class="card-grid">
<li><a href="/wonmi-gu/">원미구</a></li>
<li><a href="/sosa-gu/">소사구</a></li>
<li><a href="/ojeong-gu/">오정구</a></li>
</ul>
</section>

<section id="areas">
<h2>상동·중동·송내·역곡·원종 지역별 특징</h2>
<p>지역별 안내는 부천 대표 동 기준으로 구성됩니다. 심곡1동·심곡2동·심곡3동처럼 번호로 나뉜 행정동은 따로 페이지를 만들지 않고 심곡동·중동·상동·송내동·원종동 같은 대표 생활권으로 통합해 안내합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하기보다, 대표 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다.</p>
<ul class="card-grid">
<li><a href="/jung-dong/">중동</a></li>
<li><a href="/sang-dong/">상동</a></li>
<li><a href="/songnae-dong/">송내동</a></li>
<li><a href="/yeokgok-area/">역곡 생활권</a></li>
<li><a href="/simgok-dong/">심곡동</a></li>
<li><a href="/sosabon-dong/">소사본동</a></li>
<li><a href="/okgil-dong/">옥길동</a></li>
<li><a href="/wonjong-dong/">원종동</a></li>
<li><a href="/gogang-dong/">고강동</a></li>
</ul>
<p>중동은 신중동역과 부천시청역, 중심상권을 담당하고, 상동은 상동역·상동호수공원·부천터미널 생활권을 담당합니다. 송내동은 송내역과 중동·상동 인접권을, 역곡 생활권은 역곡역·괴안동 인접권을 담당합니다. 부천 19개 대표 지역 전체는 <a href="/wonmi-gu/">원미구</a>, <a href="/sosa-gu/">소사구</a>, <a href="/ojeong-gu/">오정구</a> 페이지에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>부천역·신중동역·상동역·소사역 역세권 안내</h2>
<p>역세권 안내는 1호선·서해선·7호선 주요 역세권을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 환승역도 노선이 여러 개라도 역명 기준 한 페이지만 운영합니다.</p>
<ul class="card-grid">
<li><a href="/station/bucheon-station/">부천역</a></li>
<li><a href="/station/sinjungdong-station/">신중동역</a></li>
<li><a href="/station/bucheon-cityhall-station/">부천시청역</a></li>
<li><a href="/station/sangdong-station/">상동역</a></li>
<li><a href="/station/songnae-station/">송내역</a></li>
<li><a href="/station/yeokgok-station/">역곡역</a></li>
<li><a href="/station/sosa-station/">소사역</a></li>
<li><a href="/station/wonjong-station/">원종역</a></li>
</ul>
<p>부천을 지나는 13개 역세권 전체는 <a href="/station/">역세권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="living">
<h2>생활권으로 위치를 찾는 방법</h2>
<p>역과 동 이름이 애매할 때는 생활권 기준이 위치를 찾기 더 쉽습니다. 신중동·부천시청, 상동역·상동호수공원, 옥길·범박, 원종·고강처럼 인접한 역과 동을 묶은 생활권 페이지에서 본인 위치에 가까운 거점을 고르시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/area/sinjungdong-cityhall/">신중동·부천시청</a></li>
<li><a href="/area/sangdong-lake-park/">상동역·상동호수공원</a></li>
<li><a href="/area/songnae-station/">송내역·송내동</a></li>
<li><a href="/area/okgil-beombak/">옥길·범박</a></li>
<li><a href="/area/wonjong-gogang/">원종·고강</a></li>
<li><a href="/area/">생활권 전체 보기</a></li>
</ul>
</section>

<section id="check">
<h2>부천시 홈타이 예약 전 확인사항</h2>
<p>부천 출장마사지 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 중동·상동처럼 접근성이 좋은 지역도 있지만 고강동, 성곡동, 옥길동, 범박동 일부는 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 예약 절차는 <a href="/reservation/">예약 안내</a>에서, 방문 전 준비는 <a href="/before-visit/">이용 전 확인사항</a>에서, 홈타이가 처음이라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>에서 확인해 주세요.</p>
</section>

<section id="dedup">
<h2>부천시 페이지 중복 방지 운영 기준</h2>
<p>부천 홈타이 안내에서 가장 중요한 부분은 번호 동을 무리하게 쪼개지 않는 것입니다. 중1동·중2동·중3동·중4동, 상1동·상2동·상3동을 각각 페이지로 만들면 본문이 비슷해질 수밖에 없습니다. 그래서 중동·상동·송내동·원종동처럼 대표 생활권으로 통합하고, 세부 번호 동은 본문 안에서 자연스럽게 설명합니다. 역세권 페이지는 부천역 페이지와 심곡동 페이지를 역세권 기준과 원도심 기준으로 분리하고, 신중동역 페이지와 중동 페이지를 다른 관점으로 작성해 같은 내용이 반복되지 않게 합니다.</p>
</section>

<section id="how">
<h2>부천시 출장마사지 사이트 이용 방법</h2>
<p>거주 지역 기준이 편하시면 구별·지역별 안내를, 역 기준이 익숙하시면 역세권 안내를, 위치 설명이 애매하면 생활권 안내를 보시면 됩니다. 어느 기준으로 들어오셔도 예약 절차와 비용 기준은 동일하며, 최종 안내는 언제나 정확한 주소를 기준으로 이루어집니다. 메인 페이지는 부천 전체 안내를 담당하고, 구별 페이지는 원미구·소사구·오정구의 큰 생활권을, 대표 지역 페이지는 중동·상동·송내동·역곡 생활권·원종동·옥길동 같은 세부 검색을 담당합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>부천시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 구별·지역별 안내 페이지에서 원미구, 소사구, 오정구 대표 지역 기준으로 확인하실 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>중동역과 신중동역은 같은 역인가요?</h3>
<p>아닙니다. 1호선 중동역과 7호선 신중동역은 다른 역입니다. 위치가 헷갈리면 가까운 역과 도로명 주소를 함께 알려주시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>상1동·상2동은 왜 페이지가 따로 없나요?</h3>
<p>번호로 나뉜 행정동은 상동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다. 방문은 행정동이 아니라 실제 주소 기준으로 진행됩니다.</p>
</div>
<div class="faq-item">
<h3>고강동·옥길동처럼 경계 지역도 방문되나요?</h3>
<p>부천시 주소라면 모두 방문 범위이며, 서울 강서·화곡, 항동 방면 경계 지역도 위치에 따라 가능할 수 있습니다. 추가 이동비 기준은 예약 시 함께 안내해 드립니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>부천 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "부천시 출장마사지｜상동·중동·송내·역곡 홈타이 지역 안내",
    "desc": "부천 출장마사지·홈타이 예약 전 상동·중동·송내·역곡·원종 생활권을 확인하세요.",
    "h1": "부천시 출장마사지 · 부천시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": "",
    "breadcrumb": [],
    "hero": _HERO,
}

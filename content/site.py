# 사이트 공통 설정 — 부천 출장마사지·홈타이 안내
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.barogo-bucheon.example.com"

BRAND = "바로 GO"
BRAND_MARK = "GO"            # 헤더 로고 원형 마크
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 텔레그램 문의 링크 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"      # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"     # 제휴문의

# 사이트 루트(부천 메인) 경로
HOME = "/gyeonggi/bucheon/"

# 상단 메뉴 — 메뉴명·URL 에 "출장마사지"를 반복하지 않는다(지역명·역명만 표시).
NAV = [
    ("부천 홈", "/gyeonggi/bucheon/", [
        ("부천시 메인", "/gyeonggi/bucheon/"),
        ("홈타이 이용 기준", "/gyeonggi/bucheon/hometai-guide/#standard"),
        ("대표 지역 선택 안내", "/gyeonggi/bucheon/#areas"),
        ("예약 전 확인사항", "/gyeonggi/bucheon/before-visit/"),
    ]),
    ("구별 안내", "/gyeonggi/bucheon/#districts", [
        ("원미구", "/gyeonggi/bucheon/wonmi-gu/"),
        ("소사구", "/gyeonggi/bucheon/sosa-gu/"),
        ("오정구", "/gyeonggi/bucheon/ojeong-gu/"),
    ]),
    ("지역별 안내", "/gyeonggi/bucheon/#areas", [
        ("심곡동", "/gyeonggi/bucheon/simgok-dong/"),
        ("원미동", "/gyeonggi/bucheon/wonmi-dong/"),
        ("역곡 생활권", "/gyeonggi/bucheon/yeokgok-area/"),
        ("춘의동", "/gyeonggi/bucheon/chunui-dong/"),
        ("도당동", "/gyeonggi/bucheon/dodang-dong/"),
        ("약대동", "/gyeonggi/bucheon/yakdae-dong/"),
        ("중동", "/gyeonggi/bucheon/jung-dong/"),
        ("상동", "/gyeonggi/bucheon/sang-dong/"),
        ("심곡본동", "/gyeonggi/bucheon/simgokbon-dong/"),
        ("소사본동", "/gyeonggi/bucheon/sosabon-dong/"),
        ("범박동", "/gyeonggi/bucheon/beombak-dong/"),
        ("옥길동", "/gyeonggi/bucheon/okgil-dong/"),
        ("괴안동", "/gyeonggi/bucheon/goean-dong/"),
        ("송내동", "/gyeonggi/bucheon/songnae-dong/"),
        ("성곡동", "/gyeonggi/bucheon/seonggok-dong/"),
        ("원종동", "/gyeonggi/bucheon/wonjong-dong/"),
        ("고강동", "/gyeonggi/bucheon/gogang-dong/"),
        ("오정동", "/gyeonggi/bucheon/ojeong-dong/"),
        ("신흥동", "/gyeonggi/bucheon/sinheung-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/bucheon/station/", [
        ("역 전체", "/gyeonggi/bucheon/station/"),
        ("부천역", "/gyeonggi/bucheon/station/bucheon-station/"),
        ("중동역", "/gyeonggi/bucheon/station/jungdong-station/"),
        ("송내역", "/gyeonggi/bucheon/station/songnae-station/"),
        ("역곡역", "/gyeonggi/bucheon/station/yeokgok-station/"),
        ("소사역", "/gyeonggi/bucheon/station/sosa-station/"),
        ("소새울역", "/gyeonggi/bucheon/station/sosaeul-station/"),
        ("까치울역", "/gyeonggi/bucheon/station/kkachiul-station/"),
        ("부천종합운동장역", "/gyeonggi/bucheon/station/bucheon-stadium-station/"),
        ("춘의역", "/gyeonggi/bucheon/station/chunui-station/"),
        ("신중동역", "/gyeonggi/bucheon/station/sinjungdong-station/"),
        ("부천시청역", "/gyeonggi/bucheon/station/bucheon-cityhall-station/"),
        ("상동역", "/gyeonggi/bucheon/station/sangdong-station/"),
        ("원종역", "/gyeonggi/bucheon/station/wonjong-station/"),
    ]),
    ("생활권 안내", "/gyeonggi/bucheon/area/", [
        ("생활권 전체", "/gyeonggi/bucheon/area/"),
        ("부천역·심곡동", "/gyeonggi/bucheon/area/bucheon-station-simgok/"),
        ("신중동·부천시청", "/gyeonggi/bucheon/area/sinjungdong-cityhall/"),
        ("상동역·상동호수공원", "/gyeonggi/bucheon/area/sangdong-lake-park/"),
        ("송내역·송내동", "/gyeonggi/bucheon/area/songnae-station/"),
        ("역곡역·역곡", "/gyeonggi/bucheon/area/yeokgok-station-area/"),
        ("소사역·소사본동", "/gyeonggi/bucheon/area/sosa-station-sosabon/"),
        ("옥길·범박", "/gyeonggi/bucheon/area/okgil-beombak/"),
        ("춘의·도당 산업", "/gyeonggi/bucheon/area/chunui-dodang/"),
        ("원종·고강", "/gyeonggi/bucheon/area/wonjong-gogang/"),
        ("오정·삼정", "/gyeonggi/bucheon/area/ojeong-samjeong/"),
        ("까치울·성곡", "/gyeonggi/bucheon/area/kkachiul-seonggok/"),
        ("부천종합운동장·여월", "/gyeonggi/bucheon/area/stadium-yeowol/"),
    ]),
    ("예약 안내", "/gyeonggi/bucheon/reservation/", [
        ("예약 가능 지역 확인", "/gyeonggi/bucheon/reservation/#area"),
        ("예약 가능 시간 안내", "/gyeonggi/bucheon/reservation/#hours"),
        ("추가 이동비 안내", "/gyeonggi/bucheon/reservation/#fee"),
        ("결제 방식 안내", "/gyeonggi/bucheon/reservation/#payment"),
        ("예약 변경 안내", "/gyeonggi/bucheon/reservation/#change"),
        ("취소 기준 안내", "/gyeonggi/bucheon/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/gyeonggi/bucheon/before-visit/", [
        ("방문 가능 주소 확인", "/gyeonggi/bucheon/before-visit/#address"),
        ("자택 이용 전 확인사항", "/gyeonggi/bucheon/before-visit/#home"),
        ("숙소 이용 전 확인사항", "/gyeonggi/bucheon/before-visit/#lodging"),
        ("오피스텔 이용 전 확인사항", "/gyeonggi/bucheon/before-visit/#officetel"),
        ("개인정보 처리 기준", "/gyeonggi/bucheon/before-visit/#privacy"),
        ("불법·선정적 서비스 불가 안내", "/gyeonggi/bucheon/before-visit/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/gyeonggi/bucheon/hometai-guide/", [
        ("홈타이란?", "/gyeonggi/bucheon/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/gyeonggi/bucheon/hometai-guide/#diff"),
        ("홈타이 이용 전 기준", "/gyeonggi/bucheon/hometai-guide/#standard"),
        ("지역별 이동 기준", "/gyeonggi/bucheon/hometai-guide/#move"),
        ("추가 비용 확인 기준", "/gyeonggi/bucheon/hometai-guide/#cost"),
        ("처음 이용하는 고객 안내", "/gyeonggi/bucheon/hometai-guide/#first"),
    ]),
    ("고객센터", "/gyeonggi/bucheon/support/", [
        ("문의하기", "/gyeonggi/bucheon/support/#contact"),
        ("자주 묻는 질문", "/gyeonggi/bucheon/support/#faq"),
        ("운영 기준", "/gyeonggi/bucheon/support/#policy"),
        ("사이트 소개", "/gyeonggi/bucheon/about/"),
        ("개인정보처리방침", "/gyeonggi/bucheon/privacy/"),
        ("이용약관", "/gyeonggi/bucheon/terms/"),
    ]),
]

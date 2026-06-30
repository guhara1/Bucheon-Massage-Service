# 사이트 공통 설정 — 부천 출장마사지·홈타이 안내
# 커스텀 도메인 연결 시 BASE_URL 을 해당 도메인으로 변경하세요.
BASE_URL = "https://bucheon-massage-service.netlify.app"

BRAND = "바로 GO"
BRAND_MARK = "GO"            # 헤더 로고 원형 마크
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 텔레그램 문의 링크 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"      # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"     # 제휴문의

# IndexNow 키 — 빙·네이버·얀덱스에 즉시 색인 통보. /<INDEXNOW_KEY>.txt 로 소유권 검증.
INDEXNOW_KEY = "740a4a73858c09af74843505c9bdc6a0"

# 사이트 루트(부천 메인) 경로
HOME = "/"

# 상단 메뉴 — 메뉴명·URL 에 "출장마사지"를 반복하지 않는다(지역명·역명만 표시).
NAV = [
    ("부천 홈", "/", [
        ("부천시 메인", "/"),
        ("홈타이 이용 기준", "/hometai-guide/#standard"),
        ("대표 지역 선택 안내", "/#areas"),
        ("예약 전 확인사항", "/before-visit/"),
    ]),
    ("구별 안내", "/#districts", [
        ("원미구", "/wonmi-gu/"),
        ("소사구", "/sosa-gu/"),
        ("오정구", "/ojeong-gu/"),
    ]),
    ("지역별 안내", "/#areas", [
        ("심곡동", "/simgok-dong/"),
        ("원미동", "/wonmi-dong/"),
        ("역곡 생활권", "/yeokgok-area/"),
        ("춘의동", "/chunui-dong/"),
        ("도당동", "/dodang-dong/"),
        ("약대동", "/yakdae-dong/"),
        ("중동", "/jung-dong/"),
        ("상동", "/sang-dong/"),
        ("심곡본동", "/simgokbon-dong/"),
        ("소사본동", "/sosabon-dong/"),
        ("범박동", "/beombak-dong/"),
        ("옥길동", "/okgil-dong/"),
        ("괴안동", "/goean-dong/"),
        ("송내동", "/songnae-dong/"),
        ("성곡동", "/seonggok-dong/"),
        ("원종동", "/wonjong-dong/"),
        ("고강동", "/gogang-dong/"),
        ("오정동", "/ojeong-dong/"),
        ("신흥동", "/sinheung-dong/"),
    ]),
    ("역세권 안내", "/station/", [
        ("역 전체", "/station/"),
        ("부천역", "/station/bucheon-station/"),
        ("중동역", "/station/jungdong-station/"),
        ("송내역", "/station/songnae-station/"),
        ("역곡역", "/station/yeokgok-station/"),
        ("소사역", "/station/sosa-station/"),
        ("소새울역", "/station/sosaeul-station/"),
        ("까치울역", "/station/kkachiul-station/"),
        ("부천종합운동장역", "/station/bucheon-stadium-station/"),
        ("춘의역", "/station/chunui-station/"),
        ("신중동역", "/station/sinjungdong-station/"),
        ("부천시청역", "/station/bucheon-cityhall-station/"),
        ("상동역", "/station/sangdong-station/"),
        ("원종역", "/station/wonjong-station/"),
    ]),
    ("생활권 안내", "/area/", [
        ("생활권 전체", "/area/"),
        ("부천역·심곡동", "/area/bucheon-station-simgok/"),
        ("신중동·부천시청", "/area/sinjungdong-cityhall/"),
        ("상동역·상동호수공원", "/area/sangdong-lake-park/"),
        ("송내역·송내동", "/area/songnae-station/"),
        ("역곡역·역곡", "/area/yeokgok-station-area/"),
        ("소사역·소사본동", "/area/sosa-station-sosabon/"),
        ("옥길·범박", "/area/okgil-beombak/"),
        ("춘의·도당 산업", "/area/chunui-dodang/"),
        ("원종·고강", "/area/wonjong-gogang/"),
        ("오정·삼정", "/area/ojeong-samjeong/"),
        ("까치울·성곡", "/area/kkachiul-seonggok/"),
        ("부천종합운동장·여월", "/area/stadium-yeowol/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#area"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#fee"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/before-visit/", [
        ("방문 가능 주소 확인", "/before-visit/#address"),
        ("자택 이용 전 확인사항", "/before-visit/#home"),
        ("숙소 이용 전 확인사항", "/before-visit/#lodging"),
        ("오피스텔 이용 전 확인사항", "/before-visit/#officetel"),
        ("개인정보 처리 기준", "/before-visit/#privacy"),
        ("불법·선정적 서비스 불가 안내", "/before-visit/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/hometai-guide/", [
        ("홈타이란?", "/hometai-guide/#what"),
        ("출장마사지와 홈타이 차이", "/hometai-guide/#diff"),
        ("홈타이 이용 전 기준", "/hometai-guide/#standard"),
        ("지역별 이동 기준", "/hometai-guide/#move"),
        ("추가 비용 확인 기준", "/hometai-guide/#cost"),
        ("처음 이용하는 고객 안내", "/hometai-guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보처리방침", "/privacy/"),
        ("이용약관", "/terms/"),
    ]),
]

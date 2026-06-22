# 전체 페이지 목록 집계 — 부천 출장마사지·홈타이
from . import (main, area_wonmi, area_sosa, area_ojeong,
               stations, livingareas, info, about)

PAGES = (
    [main.PAGE]
    + area_wonmi.PAGES
    + area_sosa.PAGES
    + area_ojeong.PAGES
    + stations.PAGES
    + livingareas.PAGES
    + info.PAGES
    + [about.PAGE]
)

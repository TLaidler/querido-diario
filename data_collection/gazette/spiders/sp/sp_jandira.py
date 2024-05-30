from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJandiraSpider(DospGazetteSpider):
    TERRITORY_ID = "3525003"
    name = "sp_jandira"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/jandira"]
    start_date = date(2022, 3, 22)

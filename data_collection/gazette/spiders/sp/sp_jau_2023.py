from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJauSpider_2023(DospGazetteSpider):
    TERRITORY_ID = "3525300"
    name = "sp_jau_2023"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/jau"]
    start_date = date(2023, 1, 6)

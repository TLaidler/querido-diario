from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpAracatubaSpider(DospGazetteSpider):
    TERRITORY_ID = "3502804"
    name = "sp_aracatuba"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/aracatuba"]
    start_date = date(2020, 4, 22)

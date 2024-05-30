from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpRioClaroSpider(DospGazetteSpider):
    TERRITORY_ID = "3543907"
    name = "sp_rio_claro"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/rio_claro"]
    start_date = date(2023, 6, 21)

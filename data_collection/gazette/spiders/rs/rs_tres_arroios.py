from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class RsTresArroiosSpider(DospGazetteSpider):
    TERRITORY_ID = "4321634"
    name = "rs_tres_arroios"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/tres_arroios"]
    start_date = date(2017, 4, 26)

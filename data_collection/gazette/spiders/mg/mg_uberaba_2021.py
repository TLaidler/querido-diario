import datetime as dt

from gazette.spiders.base.dosp import DospGazetteSpider


class MgUberabaSpider(DospGazetteSpider):
    TERRITORY_ID = "3170107"
    name = "mg_uberaba_2021"
    start_urls = ["https://www.imprensaoficialmunicipal.com.br/uberaba"]
    start_date = dt.date(2021, 9, 1)

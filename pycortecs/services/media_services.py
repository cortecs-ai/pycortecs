from pycortecs.utility.utils import validate_endpoint
from pycortecs.services import BASE_URL
from pycortecs.services.base_services import BaseServices

SENTIMENT = 'sentiment'
VOLUME = 'socialVolume'
BALANCE = 'socialBalance'
DOMINANCE = 'socialDominance'
ENDPOINTS = 'endpointInfo'
SIGNALS = 'signalInfo'
ASSETS = 'assetInfo'
PROVIDED_SINCE = 'providedSince'

API_URL = "{}/api/v1".format(BASE_URL)


class MediaServices(BaseServices):

    def __init__(self, username: str = None, password: str = None):
        super().__init__(username, password)

    def get_provided_assets(self):
        url = "{url}/{feature}".format(url=API_URL,
                                       feature=ASSETS)
        res = self._get(url, headers=self._token_header)
        return res

    def get_provided_signals(self):
        url = "{url}/{feature}".format(url=API_URL,
                                       feature=SIGNALS)
        res = self._get(url, headers=self._token_header)
        return res

    def get_provided_endpoints(self):
        url = "{url}/{feature}".format(url=API_URL,
                                       feature=ENDPOINTS)
        res = self._get(url, headers=self._token_header)
        return res

    def get_asset_provided_since(self,
                                 asset: str = 'btc',
                                 endpoint: str = 'twitter'):
        validate_endpoint(endpoint)

        url = "{url}/{provided_since}/{endpoint}".format(url=API_URL,
                                                         provided_since=PROVIDED_SINCE,
                                                         endpoint=endpoint)
        query_parameters = "?asset={asset}".format(asset=asset)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_sentiment(self,
                      endpoint: str = 'twitter',
                      since: str = None,
                      until: str = None,
                      asset: str = None,
                      interval: str = '1d') -> dict:
        validate_endpoint(endpoint)

        url = "{url}/{signal}/{endpoint}".format(url=API_URL,
                                                 signal=SENTIMENT,
                                                 endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_volume(self,
                   endpoint: str = 'twitter',
                   since: str = None,
                   until: str = None,
                   asset: str = None,
                   interval: str = '1d') -> dict:
        validate_endpoint(endpoint)

        url = "{url}/{signal}/{endpoint}".format(url=API_URL,
                                                 signal=VOLUME,
                                                 endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_dominance(self,
                      endpoint: str = 'twitter',
                      since: str = None,
                      until: str = None,
                      asset: str = None,
                      interval: str = '1d') -> dict:
        validate_endpoint(endpoint)

        url = "{url}/{signal}/{endpoint}".format(url=API_URL,
                                                 signal=DOMINANCE,
                                                 endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_balance(self,
                    endpoint: str = 'twitter',
                    since: str = None,
                    until: str = None,
                    asset: str = None,
                    interval: str = '1d',
                    threshold: float = 0.7) -> dict:
        validate_endpoint(endpoint)

        url = "{url}/{signal}/{endpoint}".format(url=API_URL,
                                                 signal=BALANCE,
                                                 endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}&threshold={threshold}".format(
            since=since,
            until=until,
            asset=asset,
            interval=interval,
            threshold=threshold)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

from utility.enumerations import MediaEndpointType, MediaSignalType
from utility.exceptions.not_specified_error import EndpointNotSpecifiedError, ModelNotSpecifiedError
from webservices.base_services import BaseServices

MEDIA_URL = "{base_url}/api/{signal}/{endpoint}"
PROVIDED_FEATURES_URL = "{base_url}/api/{feature}"


class MediaServices(BaseServices):

    def __init__(self, username, password):
        super().__init__(username, password)
        self._sentiment = "sentiment"
        self._volume = "volume"
        self._balance = "balance"
        self._dominance = "dominance"
        self._endpoints = "endpoints"
        self._signals = "signals"
        self._assets = "assets"

    def get_provided_assets(self):
        url = PROVIDED_FEATURES_URL.format(base_url=self._base_url,
                                           feature=self._assets)

        res = self._get(url, headers=self._token_header)
        return res

    def get_provided_signals(self):
        url = PROVIDED_FEATURES_URL.format(base_url=self._base_url,
                                           feature=self._signals)

        res = self._get(url, headers=self._token_header)
        return res

    def get_provided_endpoints(self):
        url = PROVIDED_FEATURES_URL.format(base_url=self._base_url,
                                           feature=self._endpoints)

        res = self._get(url, headers=self._token_header)
        return res

    def get_sentiment(self,
                      endpoint_type: MediaEndpointType = MediaEndpointType.NOT_SPECIFIED,
                      since: str = None,
                      until: str = None,
                      asset: str = None,
                      interval: str = '1d') -> dict:

        if endpoint_type == MediaEndpointType.TWITTER:
            endpoint = 'twitter'
        elif endpoint_type == MediaEndpointType.NEWS:
            endpoint = 'news'
        elif endpoint_type == MediaEndpointType.REDDIT:
            endpoint = 'reddit'
        else:
            raise EndpointNotSpecifiedError()

        url = MEDIA_URL.format(base_url=self._base_url,
                               signal='sentiment',
                               endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_volume(self,
                   endpoint_type: MediaEndpointType = MediaEndpointType.NOT_SPECIFIED,
                   since: str = None,
                   until: str = None,
                   asset: str = None,
                   interval: str = '1d') -> dict:

        if endpoint_type == MediaEndpointType.TWITTER:
            endpoint = 'twitter'
        elif endpoint_type == MediaEndpointType.NEWS:
            endpoint = 'news'
        elif endpoint_type == MediaEndpointType.REDDIT:
            endpoint = 'reddit'
        else:
            raise EndpointNotSpecifiedError()

        url = MEDIA_URL.format(base_url=self._base_url,
                               signal='volume',
                               endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_dominance(self,
                      endpoint_type: MediaEndpointType = MediaEndpointType.NOT_SPECIFIED,
                      since: str = None,
                      until: str = None,
                      asset: str = None,
                      interval: str = '1d') -> dict:

        if endpoint_type == MediaEndpointType.TWITTER:
            endpoint = 'twitter'
        elif endpoint_type == MediaEndpointType.NEWS:
            endpoint = 'news'
        elif endpoint_type == MediaEndpointType.REDDIT:
            endpoint = 'reddit'
        else:
            raise EndpointNotSpecifiedError()

        url = MEDIA_URL.format(base_url=self._base_url,
                               signal='dominance',
                               endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}".format(since=since,
                                                                                                   until=until,
                                                                                                   asset=asset,
                                                                                                   interval=interval)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

    def get_balance(self,
                    endpoint_type: MediaEndpointType = MediaEndpointType.NOT_SPECIFIED,
                    since: str = None,
                    until: str = None,
                    asset: str = None,
                    interval: str = '1d',
                    threshold: float = 0.7) -> dict:

        if endpoint_type == MediaEndpointType.TWITTER:
            endpoint = 'twitter'
        elif endpoint_type == MediaEndpointType.NEWS:
            endpoint = 'news'
        elif endpoint_type == MediaEndpointType.REDDIT:
            endpoint = 'reddit'
        else:
            raise EndpointNotSpecifiedError()

        url = MEDIA_URL.format(base_url=self._base_url,
                               signal='balance',
                               endpoint=endpoint)
        query_parameters = "?since={since}&until={until}&asset={asset}&interval={interval}&threshold={threshold}".format(
            since=since,
            until=until,
            asset=asset,
            interval=interval,
            threshold=threshold)
        res = self._get(url + query_parameters, headers=self._token_header)
        return res

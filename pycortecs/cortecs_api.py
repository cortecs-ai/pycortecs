from pycortecs.services.media_services import MediaServices
from pycortecs.utility.utils import res_to_pandas


class CortecsApi:
    def __init__(self, username: str = None, password: str = None):
        self._services = MediaServices(username, password)

    def get_provided_assets(self):
        return self._services.get_provided_assets()

    def get_provided_signals(self):
        return self._services.get_provided_signals()

    def get_provided_endpoints(self):
        return self._services.get_provided_endpoints()

    def asset_provided_since(self, asset: str = 'btc', endpoint: str = 'twitter'):
        return self._services.get_asset_provided_since(asset=asset, endpoint=endpoint)

    def get_twitter_sentiment(self,
                              since: any = None,
                              until: any = None,
                              asset: str = 'btc',
                              interval: str = '1d'):
        res = self._services.get_sentiment(endpoint='twitter',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_twitter_volume(self,
                           since: any = None,
                           until: any = None,
                           asset: str = 'btc',
                           interval: str = '1d'):
        res = self._services.get_volume(endpoint='twitter',
                                        since=since,
                                        until=until,
                                        asset=asset,
                                        interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_twitter_balance(self,
                            since: any = None,
                            until: any = None,
                            asset: str = 'btc',
                            interval: str = '1d',
                            threshold: float = 0.7):
        res = self._services.get_balance(endpoint='twitter',
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval,
                                         threshold=threshold)
        if res:
            return res_to_pandas(res)
        return None

    def get_twitter_dominance(self,
                              since: any = None,
                              until: any = None,
                              asset: str = 'btc',
                              interval: str = '1d'):
        res = self._services.get_dominance(endpoint='twitter',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_news_sentiment(self,
                           since: any = None,
                           until: any = None,
                           asset: str = 'btc',
                           interval: str = '1d'):
        res = self._services.get_sentiment(endpoint='news',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_news_volume(self,
                        since: any = None,
                        until: any = None,
                        asset: str = 'btc',
                        interval: str = '1d'):
        res = self._services.get_volume(endpoint='news',
                                        since=since,
                                        until=until,
                                        asset=asset,
                                        interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_news_balance(self,
                         since: any = None,
                         until: any = None,
                         asset: str = 'btc',
                         interval: str = '1d',
                         threshold: float = 0.7):
        res = self._services.get_balance(endpoint='news',
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval,
                                         threshold=threshold)
        if res:
            return res_to_pandas(res)
        return None

    def get_news_dominance(self,
                           since: any = None,
                           until: any = None,
                           asset: str = 'btc',
                           interval: str = '1d'):
        res = self._services.get_dominance(endpoint='news',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_reddit_sentiment(self,
                             since: any = None,
                             until: any = None,
                             asset: str = 'btc',
                             interval: str = '1d'):
        res = self._services.get_sentiment(endpoint='reddit',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_reddit_volume(self,
                          since: any = None,
                          until: any = None,
                          asset: str = 'btc',
                          interval: str = '1d'):
        res = self._services.get_volume(endpoint='reddit',
                                        since=since,
                                        until=until,
                                        asset=asset,
                                        interval=interval)
        if res:
            return res_to_pandas(res)
        return None

    def get_reddit_balance(self,
                           since: any = None,
                           until: any = None,
                           asset: str = 'btc',
                           interval: str = '1d',
                           threshold: float = 0.7):
        res = self._services.get_balance(endpoint='reddit',
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval,
                                         threshold=threshold)
        if res:
            return res_to_pandas(res)
        return None

    def get_reddit_dominance(self,
                             since: any = None,
                             until: any = None,
                             asset: str = 'btc',
                             interval: str = '1d'):
        res = self._services.get_dominance(endpoint='reddit',
                                           since=since,
                                           until=until,
                                           asset=asset,
                                           interval=interval)
        if res:
            return res_to_pandas(res)
        return None

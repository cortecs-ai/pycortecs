from utility.enumerations import MediaEndpointType, MediaSignalType
from webservices.media_services import MediaServices
import pandas as pd

# interpolate known leaks
# but do not interpolate any other nans
# because other nans might be valid (if no data is present for certain intervals)
twitter_leaks = [('2020-05-07', '2020-05-13'),
                 ('2020-11-04', '2020-11-05'),
                 ('2020-12-31', '2021-01-04')]
def fill_twitter_leaks(data: pd.Series) -> pd.Series:
    data_filled = data.interpolate('linear', limit_direction='forward')
    leaky_indices = []
    for start, stop in twitter_leaks:
        leaky_indices.extend(data[start:stop].index)
    data[leaky_indices] = data_filled[leaky_indices]
    return data

def res_to_pandas(res: dict) -> pd.Series:
    data = pd.DataFrame(res['values']).set_index('timestamp')
    data.index = pd.to_datetime(data.index, utc=True, unit='ms')
    data = data['value'].asfreq(res['interval'])
    data.name = res['signal']
    return data

class CortecsApi:
    def __init__(self, username, password):
        self._services = MediaServices(username, password)

    def me(self):
        return self._services.me()

    def get_provided_assets(self):
        return self._services.get_provided_assets()

    def get_provided_signals(self):
        return self._services.get_provided_signals()

    def get_provided_endpoints(self):
        return self._services.get_provided_endpoints()

    def get_twitter_sentiment(self, since: str = None, until: str = None, asset: str = 'btc',
                              interval: str = '1d') -> pd.Series:
        res = self._services.get_sentiment(endpoint_type=MediaEndpointType.TWITTER,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        data = res_to_pandas(res)
        data = fill_twitter_leaks(data)
        return data.ffill()  # if no data, use prev. value

    def get_twitter_volume(self, since: str = None, until: str = None, asset: str = 'btc',
                           interval: str = '1d') -> pd.Series:
        res = self._services.get_volume(endpoint_type=MediaEndpointType.TWITTER,
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval)
        data = res_to_pandas(res)
        data = fill_twitter_leaks(data)
        return data.fillna(0)  # if no data, volume is zero

    def get_twitter_balance(self, since: str = None, until: str = None, asset: str = 'btc',
                            interval: str = '1d', threshold: float = 0.7) -> pd.Series:
        res = self._services.get_balance(endpoint_type=MediaEndpointType.TWITTER,
                                          since=since,
                                          until=until,
                                          asset=asset,
                                          interval=interval,
                                          threshold=threshold)
        data = res_to_pandas(res)
        return fill_twitter_leaks(data)

    def get_twitter_dominance(self, since: str = None, until: str = None, asset: str = 'btc',
                              interval: str = '1d') -> pd.Series:
        res = self._services.get_dominance(endpoint_type=MediaEndpointType.TWITTER,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        data = res_to_pandas(res)
        return fill_twitter_leaks(data)

    def get_news_sentiment(self, since: str = None, until: str = None, asset: str = 'btc',
                           interval: str = '1d') -> pd.Series:
        res = self._services.get_sentiment(endpoint_type=MediaEndpointType.NEWS,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        data = res_to_pandas(res)
        return fill_twitter_leaks(data)

    def get_news_volume(self, since: str = None, until: str = None, asset: str = 'btc',
                        interval: str = '1d') -> pd.Series:
        res = self._services.get_volume(endpoint_type=MediaEndpointType.NEWS,
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval)
        data = res_to_pandas(res)
        return fill_twitter_leaks(data)

    def get_news_balance(self, since: str = None, until: str = None, asset: str = 'btc',
                         interval: str = '1d', threshold: float = 0.7) -> pd.Series:
        res = self._services.get_balance(endpoint_type=MediaEndpointType.NEWS,
                                          since=since,
                                          until=until,
                                          asset=asset,
                                          interval=interval,
                                          threshold=threshold)
        return res_to_pandas(res)

    def get_news_dominance(self, since: str = None, until: str = None, asset: str = 'btc',
                           interval: str = '1d') -> pd.Series:
        res = self._services.get_dominance(endpoint_type=MediaEndpointType.NEWS,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        return res_to_pandas(res)

    def get_reddit_sentiment(self, since: str = None, until: str = None, asset: str = 'btc',
                             interval: str = '1d') -> pd.Series:
        res = self._services.get_sentiment(endpoint_type=MediaEndpointType.REDDIT,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        return res_to_pandas(res)

    def get_reddit_volume(self, since: str = None, until: str = None, asset: str = 'btc',
                          interval: str = '1d') -> pd.Series:
        res = self._services.get_volume(endpoint_type=MediaEndpointType.REDDIT,
                                         since=since,
                                         until=until,
                                         asset=asset,
                                         interval=interval)
        return res_to_pandas(res)

    def get_reddit_balance(self, since: str = None, until: str = None, asset: str = 'btc',
                           interval: str = '1d', threshold: float = 0.7) -> pd.Series:
        res = self._services.get_balance(endpoint_type=MediaEndpointType.REDDIT,
                                          since=since,
                                          until=until,
                                          asset=asset,
                                          interval=interval,
                                          threshold=threshold)
        return res_to_pandas(res)

    def get_reddit_dominance(self, since: str = None, until: str = None, asset: str = 'btc',
                             interval: str = '1d') -> pd.Series:
        res = self._services.get_dominance(endpoint_type=MediaEndpointType.REDDIT,
                                            since=since,
                                            until=until,
                                            asset=asset,
                                            interval=interval)
        return res_to_pandas(res)

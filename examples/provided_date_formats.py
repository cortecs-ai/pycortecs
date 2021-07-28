from pycortecs.cortecs_api import CortecsApi
from pprint import pprint


def main():
    """
    The example shows all provided date formats
    """
    api = CortecsApi()

    btc_twitter_ymd = api.get_twitter_sentiment(since="2021-03-01",
                                                until="2021-03-05",
                                                asset='btc',
                                                interval='1d')
    pprint(btc_twitter_ymd)

    # get result as dict
    btc_twitter_ymdhms = api.get_twitter_sentiment(since="2021-03-01 00:00:00",
                                                   until="2021-03-05 10:05:03",
                                                   asset='btc',
                                                   interval='1d')
    pprint(btc_twitter_ymdhms)

    # get result as dict
    btc_twitter_ts = api.get_twitter_sentiment(since=1614556800,
                                               until=1614902400,
                                               asset='btc',
                                               interval='1d')
    pprint(btc_twitter_ts)


if __name__ == '__main__':
    main()

from pycortecs.cortecs_api import CortecsApi
from pprint import pprint


def main():
    """
    The example shows how to get dominance for different endpoints and assets
    """
    api = CortecsApi()

    since = "2021-03-01"
    until = "2021-03-05"

    dominance_twitter_btc = api.get_twitter_dominance(since=since,
                                                      until=until,
                                                      asset='btc',
                                                      interval='1d')
    pprint(dominance_twitter_btc)

    dominance_news_eth = api.get_news_dominance(since=since,
                                                until=until,
                                                asset='eth',
                                                interval='1d')
    pprint(dominance_news_eth)

    dominance_reddit_xrp = api.get_reddit_dominance(since=since,
                                                    until=until,
                                                    asset='xrp',
                                                    interval='1d')
    pprint(dominance_reddit_xrp)


if __name__ == '__main__':
    main()

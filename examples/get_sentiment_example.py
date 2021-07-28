from pycortecs.cortecs_api import CortecsApi
from pprint import pprint


def main():
    """
    The example shows how to get sentiment for different endpoints and assets
    """
    api = CortecsApi()

    since = "2021-03-01"
    until = "2021-03-05"

    sentiment_twitter_btc = api.get_twitter_sentiment(since=since,
                                                      until=until,
                                                      asset='btc',
                                                      interval='1d')
    pprint(sentiment_twitter_btc)

    sentiment_news_eth = api.get_news_sentiment(since=since,
                                                until=until,
                                                asset='eth',
                                                interval='1d')
    pprint(sentiment_news_eth)

    sentiment_reddit_xrp = api.get_reddit_sentiment(since=since,
                                                    until=until,
                                                    asset='xrp',
                                                    interval='1d')
    pprint(sentiment_reddit_xrp)


if __name__ == '__main__':
    main()

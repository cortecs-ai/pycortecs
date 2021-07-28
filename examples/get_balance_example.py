from pycortecs.cortecs_api import CortecsApi
from pprint import pprint


def main():
    """
    The example shows how to get balance for different endpoints and assets

    The social balance is the difference of
        sum(messages) with sentiment > threshold) - sum(messages) with sentiment < 1 - threshold
    """
    api = CortecsApi()

    since = "2021-03-01"
    until = "2021-03-05"

    balance_twitter_btc = api.get_twitter_balance(since=since,
                                                  until=until,
                                                  asset='btc',
                                                  interval='1d',
                                                  threshold=0.8)
    pprint(balance_twitter_btc)

    balance_news_eth = api.get_news_balance(since=since,
                                            until=until,
                                            asset='eth',
                                            interval='1d',
                                            threshold=0.8)
    pprint(balance_news_eth)

    balance_reddit_xrp = api.get_reddit_balance(since=since,
                                                until=until,
                                                asset='xrp',
                                                interval='1d',
                                                threshold=0.55)
    pprint(balance_reddit_xrp)


if __name__ == '__main__':
    main()

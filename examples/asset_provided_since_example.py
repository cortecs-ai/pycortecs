from pycortecs.cortecs_api import CortecsApi
from pprint import pprint



def main():
    """
    The example shows how to see since when an asset is provided for a specific endpoint.
    As can be seen, this is different for different endpoints
    """
    api = CortecsApi()

    btc_twitter = api.asset_provided_since('btc', 'twitter')
    pprint(btc_twitter)

    btc_news = api.asset_provided_since('btc', 'news')
    pprint(btc_news)

    btc_reddit = api.asset_provided_since('btc', 'reddit')
    pprint(btc_reddit)


if __name__ == '__main__':
    main()
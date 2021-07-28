from pycortecs.cortecs_api import CortecsApi
from pprint import pprint



def main():
    """
    The example shows how to connect to to cortecs-api and how to get provided assets, signals and endpoints
    """
    api = CortecsApi()

    assets = api.get_provided_assets()
    pprint(assets)

    signals = api.get_provided_signals()
    pprint(signals)

    endpoints = api.get_provided_endpoints()
    pprint(endpoints)


if __name__ == '__main__':
    main()

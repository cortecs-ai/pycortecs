from api.cortecs_api import CortecsApi
from binance.client import Client
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.vector_ar.var_model import VAR
from sklearn.metrics import accuracy_score

exchange = Client()
crtcs = CortecsApi('gt', 'gt')  # todo use proper credentials
interval, since, until = '1d', "2019-11-01", "2021-01-16"
assets = ['btc', 'eth', 'ltc', 'xrp', 'link', 'bnb', 'trx', 'xlm', 'xtz', 'ada', 'iota', 'eos', 'xmr',
          'dash', 'neo', 'atom', 'zec', 'ont', 'bat', 'vet']

def get_returns(asset, interval, since, until):
    klines = pd.DataFrame(exchange.get_historical_klines(f"{asset.upper()}USDT", interval, since, until))
    price = klines[1].astype('float')
    price.index = pd.to_datetime(klines[0], utc=True, unit='ms')
    price.name = 'return'
    return price.pct_change().asfreq(interval)[1:]

# get price weighted index (bitcoin and ethereum)
def get_crypto_index(interval, since, until):
    bitcoin = get_returns('btc', interval, since, until)
    ethereum = get_returns('eth', interval, since, until)
    return (bitcoin + ethereum) / 2

# use cortecs' twitter data to predict several cryptocurrencies
# evaluate performance against a benchmark
if __name__ == '__main__':

    overall_performance = pd.DataFrame(index=assets)
    overall_twitter_sentiment = pd.DataFrame()
    overall_twitter_volume = pd.DataFrame()

    index = get_crypto_index(interval, since, until)
    for asset in assets:
        print(f'# {asset}')

        # todo use overall sentiment and volume
        # get data # todo use defaults, see https://gitlab.com/cortecs/snap/cortecs-api/-/issues/5
        twitter_sentiment = crtcs.get_twitter_sentiment(since, until, asset, interval)
        returns = get_returns(asset, interval, since, until)
        abn_returns = returns - index

        X = pd.concat([abn_returns.shift(-1), twitter_sentiment], axis=1)
        X = X[1:-1]

        gc_res = grangercausalitytests(X, 3, verbose=False)
        print(gc_res[1][0]['ssr_ftest'][1])

    # ax = overall_performance.plot.bar(ylim=(45, 65), title='Accuracy', figsize=(6.5, 3.5), color=['grey', 'royalblue'])
    # ax.axhline(y=overall_performance['benchmark'].mean(), color='grey', linestyle='--', label='benchmark')
    # ax.axhline(y=overall_performance['twitter'].mean(), color='royalblue', linestyle='--', label='twitter')
    # ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    # plt.tight_layout()
    # plt.show()


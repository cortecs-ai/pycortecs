from api.cortecs_api import CortecsApi
from binance.client import Client
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.vector_ar.var_model import VAR
from sklearn.metrics import accuracy_score

exchange = Client()
crtcs = CortecsApi('gt', 'gt')  # todo use proper credentials
assets = ['btc', 'eth', 'ltc', 'xrp', 'link', 'bnb', 'trx', 'xlm', 'xtz', 'ada', 'iota', 'eos', 'xmr',
          'dash', 'neo', 'atom', 'zec', 'ont', 'bat', 'vet']

def get_returns(asset, interval, since, until):
    klines = pd.DataFrame(exchange.get_historical_klines(f"{asset.upper()}USDT", interval, since, until))
    price = klines[1].astype('float')
    price.index = pd.to_datetime(klines[0], utc=True, unit='ms')
    price.name = 'return'
    return price.pct_change().asfreq(interval)[1:]

# use cortecs' twitter data to predict several cryptocurrencies
# evaluate performance against a benchmark
if __name__ == '__main__':

    overall_performance = pd.DataFrame(index=assets)
    overall_twitter_sentiment = pd.DataFrame()
    overall_twitter_volume = pd.DataFrame()
    for asset in assets:
        print(f'# {asset}')

        # todo use overall sentiment and volume
        # get data # todo use defaults, see https://gitlab.com/cortecs/snap/cortecs-api/-/issues/5
        interval, since, until = '1d', "2019-11-01", "2021-01-16"
        twitter_sentiment = crtcs.get_twitter_sentiment(since, until, asset, interval)
        twitter_volume = crtcs.get_twitter_volume(since, until, asset, interval)
        returns = get_returns(asset, interval, since, until)

        X = pd.concat([twitter_sentiment, twitter_volume, returns], axis=1)
        y = returns.shift(-1)
        X, y = X[:-1], y[:-1]

        # rolling VAR forecast
        # a model is fitted over a training period and only the next day after this period is predicted
        # then the window is shifted by one, the model is trained again and the next day is predicted
        # this setting works in highly dynamic environments (such as finance ;-))
        train_period = 120
        var_lag = 2
        y_test = y[train_period:]
        y_benchmark_hat_test = pd.Series(index=y_test.index, dtype='float')
        y_twitter_hat_test = pd.Series(index=y_test.index, dtype='float')
        for t in range(len(X) - train_period):
            train_batch_idx = X.index[t:t + train_period]
            ar = AutoReg(returns[train_batch_idx].values, lags=var_lag, old_names=False).fit()

            var = VAR(X.loc[train_batch_idx].values)
            var_fit = var.fit(maxlags=var_lag, trend='c')

            day_to_predict = train_batch_idx[-1] + pd.Timedelta('1d')
            y_benchmark_hat_test[day_to_predict] = ar.forecast(1)[0]
            y_twitter_hat_test[day_to_predict] = var_fit.forecast(X.loc[train_batch_idx][-var_lag:].values, 1)[0][-1]

        # neglect noise and remove predicted returns smaller than 1%
        small_benchmark_changes = y_benchmark_hat_test.abs() < .01
        small_twitter_changes = y_twitter_hat_test.abs() < .01
        overall_performance.loc[asset, 'benchmark'] = accuracy_score(y_test[~small_benchmark_changes] > 0, y_benchmark_hat_test[~small_benchmark_changes] > 0) * 100
        print(f"price only {overall_performance.loc[asset, 'benchmark']}")
        overall_performance.loc[asset, 'twitter'] = accuracy_score(y_test[~small_twitter_changes] > 0, y_twitter_hat_test[~small_twitter_changes] > 0) * 100
        print(f"twitter {overall_performance.loc[asset, 'twitter']}")
        # overall_performance.loc[asset, 'benchmark'] = accuracy_score(y_test > 0, y_benchmark_hat_test > 0) * 100
        # print(f"price only {overall_performance.loc[asset, 'benchmark']}")
        # overall_performance.loc[asset, 'twitter'] = accuracy_score(y_test > 0, y_twitter_hat_test > 0) * 100
        # print(f"twitter {overall_performance.loc[asset, 'twitter']}")

    ax = overall_performance.plot.bar(ylim=(45, 65), title='Accuracy', figsize=(6.5, 3.5), color=['grey', 'royalblue'])
    ax.axhline(y=overall_performance['benchmark'].mean(), color='grey', linestyle='--', label='benchmark')
    ax.axhline(y=overall_performance['twitter'].mean(), color='royalblue', linestyle='--', label='twitter')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.tight_layout()
    plt.show()


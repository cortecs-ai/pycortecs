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

def get_returns(symbol, interval, since, until):
    klines = pd.DataFrame(exchange.get_historical_klines(symbol, interval, since, until))
    price = klines[1].astype('float')
    price.index = pd.to_datetime(klines[0], utc=True, unit='ms')
    price.name = 'return'
    return price.pct_change().asfreq(interval)[1:]

# use cortecs' twitter data to predict several cryptocurrencies
# evaluate performance against a benchmark
if __name__ == '__main__':

    # get data
    interval, since, until = '1d', "2019-11-01", "2021-01-16"
    twitter_sentiment = crtcs.get_twitter_sentiment(since, until, 'btc', interval)
    twitter_volume = crtcs.get_twitter_volume(since, until, 'btc', interval)
    returns = get_returns('BTCUSDT', interval, since, until)

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

    # # neglect noise
    # # remove predicted returns smaller than 1%
    # noise_benchmark = y_benchmark_hat_test.abs() < .01
    # noise_twitter = y_twitter_hat_test.abs() < .01
    # hitrate_benchmark = accuracy_score(y_test[~noise_benchmark] > 0, y_benchmark_hat_test[~noise_benchmark] > 0) * 100
    # print(f"price only {hitrate_benchmark} hitrate")
    # hitrate_twitter = accuracy_score(y_test[~noise_twitter] > 0, y_twitter_hat_test[~noise_twitter] > 0) * 100
    # print(f"twitter {hitrate_twitter} hitrate")

    hitrate_benchmark = accuracy_score(y_test > 0, y_benchmark_hat_test > 0) * 100
    print(f"price only {hitrate_benchmark} hitrate")
    hitrate_twitter = accuracy_score(y_test > 0, y_twitter_hat_test > 0) * 100
    print(f"twitter {hitrate_twitter} hitrate")


    # long short strategy
    returns_test = returns[train_period:-1]
    benchmark_trades = (y_benchmark_hat_test > 0) * 2 - 1
    benchmark_returns = benchmark_trades * returns_test
    twitter_trades = (y_twitter_hat_test > 0) * 2 - 1
    twitter_returns = twitter_trades * returns_test

    cum_returns = pd.DataFrame({'bitcoin': returns_test.cumsum(),
                                'benchmark': benchmark_returns.cumsum(),
                                'twitter': twitter_returns.cumsum()})
    ax = cum_returns.plot()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.legend(loc=4)
    plt.show()




PyCortecs is a python wrapper for the [CortecsApi](http://185.232.71.249:8002)


PyCortecs provides a number of aggregated signals for crypto traders and everybody that is interested in cryto:
- sentiment
- socialVolume
- socialDominance
- socialBalance

These signals are provided for three different sources:
- twitter
- news
- reddit

86 assets are provided at the moment.

Most of the functionality can be seen in the [examples](https://gitlab.com/cortecs/snap/pycortecs/-/tree/feature/update-to-latest-api-version/examples).

**Simplest way to get the sentiment:**

```python
from api.cortecs_api import CortecsApi
from pprint import pprint

api = CortecsApi()

since = "2021-03-01"
until = "2021-03-05"

sentiment_twitter_btc = api.get_twitter_sentiment(since=since,
                                                  until=until,
                                                  asset='btc',
                                                  interval='1d')
pprint(sentiment_twitter_btc)
```

**gives the output:**

```python
                          interval endpoint     signal      btc
timestamp                                                      
2021-03-02 00:00:00+00:00       1d  twitter  sentiment  0.80919
2021-03-03 00:00:00+00:00       1d  twitter  sentiment  0.82196
2021-03-04 00:00:00+00:00       1d  twitter  sentiment  0.83813
2021-03-05 00:00:00+00:00       1d  twitter  sentiment  0.81766

```

Other functionality can be seen in the [examples](https://gitlab.com/cortecs/snap/pycortecs/-/tree/feature/update-to-latest-api-version/examples).






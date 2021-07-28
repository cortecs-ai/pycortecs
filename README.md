# Cortecs - Crypto Sentiment

Cortecs gathers crypto headlines from twitter, reddit and online news to extracts the social sentiment of cryptocurrencies.
The objective is to deliver denoised sentiment metrics in realtime. Therefore, each headline is efficiently analyzed in a
filter engine to assure the data meets certain quality criteria (see [Cortecs Feed](https://cortecs.ai/chart)) before
the actual sentiment is calculated. Most modules in the filter engine are built on top
of [Transfomers](https://huggingface.co/transformers/).


![SNAP](https://github.com/cortecs-ai/pycortecs/blob/main/img/SNAP_Overview.png?raw=true "Title")

## API

PyCortecs is a python wrapper for the [CortecsApi](http://185.232.71.249:8002/redoc), which provides multiple sentiment metrics:

- sentiment
- social volume
- social dominance
- social balance

Currently 86 of the most important
cryptos are supported. Twitter sentiment dates back until 2019-11-01. News and reddit sentiment was added later on.
  
## Example

Install with `pip install pycortecs`.

```python
from pycortecs import CortecsApi
from pprint import pprint

api = CortecsApi()
## Get Bitcoin sentiment from Twitter
sentiment_twitter_btc = api.get_twitter_sentiment(since="2021-03-01",
                                                  until="2021-03-05",
                                                  asset='btc',
                                                  interval='1d')
pprint(sentiment_twitter_btc)
```

```
                          interval endpoint     signal      btc
timestamp                                                      
2021-03-02 00:00:00+00:00       1d  twitter  sentiment  0.80919
2021-03-03 00:00:00+00:00       1d  twitter  sentiment  0.82196
2021-03-04 00:00:00+00:00       1d  twitter  sentiment  0.83813
2021-03-05 00:00:00+00:00       1d  twitter  sentiment  0.81766

```

For detailed usage checkout the [docs](http://185.232.71.249:8002/docs#/) or look into
the [examples folder](https://github.com/cortecs-ai/pycortecs/tree/main/examples).

## Supported by

![University of Vienna](https://github.com/cortecs-ai/pycortecs/blob/main/img/UniVie.png "University of Vienna")
![Techhouse](https://github.com/cortecs-ai/pycortecs/blob/main/img/Techhouse.png "Techhouse")

## Social

- Follow on [Twitter](https://twitter.com/cortecs_ai)
- Contact via [LinkedIn](https://www.linkedin.com/company/cortecs-ai)
- Contact via [mail](mailto:office@cortecs.ai)







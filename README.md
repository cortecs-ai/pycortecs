```python
from api.cortecs_api import CortecsApi
from pprint import pprint
```


```python
api = CortecsApi('gt', 'gt')
```

    {'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJndCIsImV4cCI6MTYyMTA3MDAzNn0.srFE-dWJSmuL6weDgCEW0gRqeEl9Ae5H_rCMUS0bK-o', 'token_type': 'bearer'}



```python
pprint(api.me())
print("\n\n")
pprint(api.get_provided_assets())
print("\n\n")
pprint(api.get_provided_signals())
print("\n\n")
pprint(api.get_provided_endpoints())
```

    {'email': 'gt@gt.com',
     'is_active': True,
     'is_superuser': False,
     'registered_since': 1617778399848,
     'user_id': None,
     'username': 'gt'}
    
    
    
    {'assets': ['btc',
                'eth',
                'ltc',
                'xrp',
                'link',
                'bnb',
                'trx',
                'xlm',
                'xtz',
                'ada',
                'iota',
                'eos',
                'bsv',
                'bch',
                'xmr',
                'dash',
                'neo',
                'atom',
                'zec',
                'mkr',
                'ont',
                'bat',
                'vet',
                'snt',
                'uma',
                'sushi',
                'iris',
                'uni',
                'aave',
                'algo',
                'zrx',
                'dot',
                'cro',
                'hedg',
                'etc',
                'omg',
                'bal',
                'btm',
                'comp',
                'tomo',
                'theta',
                'tfuel',
                'sxp',
                'sol',
                'rune',
                'priv',
                'paxg',
                'okb',
                'mta',
                'doge',
                'ht',
                'drgn',
                'dmg',
                'bnt',
                'rep',
                'ren',
                'lrc',
                'kava',
                'knc',
                'ocean',
                'leo',
                'gt',
                'matic',
                'btmx',
                'tryb',
                'xaut',
                'brz',
                'ampl',
                'cream',
                'hnt',
                'flm',
                'avax',
                'yfi',
                'yfv',
                'yffi',
                'yfii',
                'yfiii',
                'fil',
                'chz',
                'nuls',
                'iost',
                'arpa',
                'dcr',
                'qtum',
                'xem',
                'zil'],
     'description': 'provided assets',
     'timestamp': 1621069916297}
    
    
    
    {'description': 'signals for each media endpoint provided by cortecs',
     'signals': ['sentiment', 'volume', 'balance', 'dominance'],
     'timestamp': 1621069916354}
    
    
    
    {'description': 'media endpoints provided by cortecs',
     'endpoints': ['twitter', 'news', 'reddit'],
     'timestamp': 1621069916400}



```python
pprint(api.get_twitter_sentiment("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_news_sentiment("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_reddit_sentiment("2021-02-18", "2021-02-23", "btc", "1d"))
```

    {'asset': 'btc',
     'endpoint': 'twitter',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'sentiment',
     'timestamp': 1621069916532,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 0.763645785483991},
                {'timestamp': '1610409600000', 'value': 0.6343083608553957},
                {'timestamp': '1610496000000', 'value': 0.7224203138700146},
                {'timestamp': '1610582400000', 'value': 0.7290948716742256},
                {'timestamp': '1610668800000', 'value': 0.7840293173270114}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'news',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'sentiment',
     'timestamp': 1621069916632,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 0.5958004063460975},
                {'timestamp': '1610409600000', 'value': 0.41304646105431825},
                {'timestamp': '1610496000000', 'value': 0.5713047064788692},
                {'timestamp': '1610582400000', 'value': 0.5113568325651189},
                {'timestamp': '1610668800000', 'value': 0.6698813848973563}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'reddit',
     'from_date': '2021-02-18',
     'interval': '1d',
     'signal': 'sentiment',
     'timestamp': 1621069916707,
     'to_date': '2021-02-23',
     'values': [{'timestamp': '1613692800000', 'value': 0.5662419484962832},
                {'timestamp': '1613779200000', 'value': 0.5666859431189677},
                {'timestamp': '1614038400000', 'value': 0.45356735521001895}]}



```python
pprint(api.get_twitter_volume("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_news_volume("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_reddit_volume("2021-02-18", "2021-02-23", "btc", "1d"))
```

    {'asset': 'btc',
     'endpoint': 'twitter',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'volume',
     'timestamp': 1621069916790,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 16800.0},
                {'timestamp': '1610409600000', 'value': 33032.0},
                {'timestamp': '1610496000000', 'value': 20820.0},
                {'timestamp': '1610582400000', 'value': 18623.0},
                {'timestamp': '1610668800000', 'value': 22232.0}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'news',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'volume',
     'timestamp': 1621069916861,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 60.0},
                {'timestamp': '1610409600000', 'value': 139.0},
                {'timestamp': '1610496000000', 'value': 143.0},
                {'timestamp': '1610582400000', 'value': 150.0},
                {'timestamp': '1610668800000', 'value': 156.0}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'reddit',
     'from_date': '2021-02-18',
     'interval': '1d',
     'signal': 'volume',
     'timestamp': 1621069916930,
     'to_date': '2021-02-23',
     'values': [{'timestamp': '1613692800000', 'value': 781.0},
                {'timestamp': '1613779200000', 'value': 358.0},
                {'timestamp': '1614038400000', 'value': 649.0}]}



```python
pprint(api.get_twitter_dominance("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_news_dominance("2021-01-10", "2021-01-15", "btc", "1d"))
print("\n\n")
pprint(api.get_reddit_dominance("2021-02-18", "2021-02-25", "btc", "1w"))
```

    {'asset': 'btc',
     'endpoint': 'twitter',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'dominance',
     'timestamp': 1621069917630,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 0.5383925137802846},
                {'timestamp': '1610409600000', 'value': 0.5902471275664278},
                {'timestamp': '1610496000000', 'value': 0.5393642651744773},
                {'timestamp': '1610582400000', 'value': 0.5913940933629723},
                {'timestamp': '1610668800000', 'value': 0.5886464732048294}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'news',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'dominance',
     'timestamp': 1621069917803,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 0.5357142857142857},
                {'timestamp': '1610409600000', 'value': 0.6650717703349283},
                {'timestamp': '1610496000000', 'value': 0.6651162790697674},
                {'timestamp': '1610582400000', 'value': 0.6880733944954128},
                {'timestamp': '1610668800000', 'value': 0.6265060240963856}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'reddit',
     'from_date': '2021-02-18',
     'interval': '1w',
     'signal': 'dominance',
     'timestamp': 1621069917951,
     'to_date': '2021-02-25',
     'values': [{'timestamp': '1614211200000', 'value': 0.22633031645163362}]}



```python
pprint(api.get_twitter_balance("2021-01-10", "2021-01-15", "btc", "1d", 0.7))
print("\n\n")
pprint(api.get_news_balance("2021-01-10", "2021-01-15", "btc", "1d", 0.7))
print("\n\n")
pprint(api.get_reddit_balance("2021-02-18", "2021-02-23", "btc", "1d", 0.7))
```

    {'asset': 'btc',
     'endpoint': 'twitter',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'balance',
     'threshold': 0.7,
     'timestamp': 1621069918087,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 9566.0},
                {'timestamp': '1610409600000', 'value': 9204.0},
                {'timestamp': '1610496000000', 'value': 9659.0},
                {'timestamp': '1610582400000', 'value': 9160.0},
                {'timestamp': '1610668800000', 'value': 13549.0}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'news',
     'from_date': '2021-01-10',
     'interval': '1d',
     'signal': 'balance',
     'threshold': 0.7,
     'timestamp': 1621069918180,
     'to_date': '2021-01-15',
     'values': [{'timestamp': '1610323200000', 'value': 11.0},
                {'timestamp': '1610409600000', 'value': -28.0},
                {'timestamp': '1610496000000', 'value': 22.0},
                {'timestamp': '1610582400000', 'value': 5.0},
                {'timestamp': '1610668800000', 'value': 58.0}]}
    
    
    
    {'asset': 'btc',
     'endpoint': 'reddit',
     'from_date': '2021-02-18',
     'interval': '1d',
     'signal': 'balance',
     'threshold': 0.7,
     'timestamp': 1621069918275,
     'to_date': '2021-02-23',
     'values': [{'timestamp': '1613692800000', 'value': 121.0},
                {'timestamp': '1613779200000', 'value': 56.0},
                {'timestamp': '1614038400000', 'value': -78.0}]}



```python

```

import pandas as pd
from pycortecs.utility.enumerations import EndpointType
from pycortecs.utility.exceptions.not_specified_error import EndpointNotSpecifiedError


def validate_endpoint(endpoint):
    if endpoint not in EndpointType.as_list():
        raise EndpointNotSpecifiedError()


def res_to_pandas(res: dict) -> pd.DataFrame:
    try:
        data = pd.DataFrame(res['values']).set_index('timestamp')
        data.index = pd.to_datetime(data.index, utc=True, unit='s')
        data.insert(0, 'signal', res['signal'])
        data.insert(0, 'endpoint', res['endpoint'])
        data.insert(0, 'interval', res['interval'])
        if 'threshold' in res.keys():
            data.insert(0, 'threshold', res['threshold'])

        data.name = res['signal']
        data = data.rename(columns={'value': res['asset']})
        data = data.drop(columns="datetime")
        return data
    except KeyError:
        return pd.DataFrame()

import requests
import logging
from pycortecs.utility.enumerations import StatusCode
from pycortecs.services import CONNECTION_DETAILS

log = logging.getLogger()

LOGIN = CONNECTION_DETAILS['login']


class BaseServices:

    def __init__(self, username, password):
        self._login_header = CONNECTION_DETAILS['headers']['login_header']
        self._token_header = CONNECTION_DETAILS['headers']['token_header']
        self._login_form = {'username': username, 'password': password}
        self._access_token = None
        self._token_type = None
        self._connect()

    def _connect(self):
        #authentication is disabled at the moment

        '''
        res = requests.post(BASE_URL + LOGIN, data=self._login_form, headers=self._login_header)
        try:
            self._access_token = res.json()['access_token']
            self._token_type = res.json()['token_type']
            self._set_token_header()
            return True
        except KeyError:
            raise NotConnectedError(res.status_code, res.json()['detail'])
        '''

        return True

    def _set_token_header(self):
        self._token_header['authorization'] = "{} {}".format(self._token_type, self._access_token)

    def _get(self, url, headers):
        res = requests.get(url, headers=headers)
        status_code = self._check_status_code(res.status_code)
        if status_code == StatusCode.RETRY:
            return self._get(url, headers)
        elif status_code == StatusCode.OK:
            return res.json()
        else:
            log.error(res.json())
            return None

    def _post(self, url, data, headers):
        res = requests.post(url, data=data, headers=headers)
        status_code = self._check_status_code(res.status_code)
        if status_code == StatusCode.RETRY:
            return self._post(url, data, headers)
        elif status_code == StatusCode.OK:
            return res.json()
        else:
            log.error(res.json())
            return None

    def _check_status_code(self, status_code):
        if status_code == 401:
            log.info('token expired, try to reconnect')
            self._connect()
            return StatusCode.RETRY
        elif status_code == 200:
            return StatusCode.OK
        else:
            return StatusCode.ERROR

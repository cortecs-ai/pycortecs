import requests

from utility.exceptions.not_connected_error import NotConnectedError
import logging
import yaml

from utility.enumerations import StatusCode

log = logging.getLogger()
base_conf = yaml.safe_load(open("./config.yml", 'r'))

class BaseServices:

    def __init__(self, username, password):

        self._base_url = base_conf['base_url']
        self._login = base_conf['login']
        self._my_user = base_conf['users']['my_user']
        self._login_header = base_conf['headers']['login_header']
        self._token_header = base_conf['headers']['token_header']
        self._login_form = {'username': username, 'password': password}
        self._access_token = None
        self._token_type = None
        #self._set_connection_settings()
        self._connect()


    def _connect(self):
        res = requests.post(self._base_url + self._login, data=self._login_form, headers=self._login_header)
        try:
            print(res.json())
            self._access_token = res.json()['access_token']
            self._token_type = res.json()['token_type']
            self._set_token_header()
            return True
        except KeyError:
            raise NotConnectedError(res.status_code, res.json()['detail'])

    def me(self):
        res = self._get(self._base_url + self._my_user, headers=self._token_header)
        return res

    def _set_token_header(self):
        self._token_header['authorization'] = "{} {}".format(self._token_type, self._access_token)

    def _get(self, url, headers):
        res = requests.get(url, headers=headers)
        status_code = self._check_status_code(res.status_code)
        if status_code == StatusCode.RETRY:
            self._get(url, headers)
        elif status_code == StatusCode.OK:
            return res.json()
        else:
            log.error(res.json())

    def _post(self, url, data, headers):
        res = requests.post(url, data=data, headers=headers)
        status_code = self._check_status_code(res.status_code)
        if status_code == StatusCode.RETRY:
            self._post(url, data, headers)
        elif status_code == StatusCode.OK:
            return res.json()
        else:
            log.error(res.json())

    def _check_status_code(self, status_code):
        if status_code == 401:
            log.info('token expired, try to reconnect')
            self._connect()
            return StatusCode.RETRY
        elif status_code == 200:
            return StatusCode.OK
        else:
            return StatusCode.ERROR

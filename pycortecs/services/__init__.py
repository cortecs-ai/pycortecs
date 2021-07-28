import yaml

base_conf = yaml.safe_load(open("./config.yml", 'r'))

CONNECTION_DETAILS = base_conf['server_connection']

BASE_URL = CONNECTION_DETAILS['base_url']


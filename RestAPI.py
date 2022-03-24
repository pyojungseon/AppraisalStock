# pip install requests

import requests
import json
import configparser


class RestAPI:

    env = None
    props = None

    def __init__(self, _env):
        print("RestAPI Constructor : %s" % _env)
        self.env = _env
        self.props = self.getConfig(_env)

    def __del__(self):
        print("RestAPI Destructor")

    def getConfig(self, env):
        properties = configparser.ConfigParser()
        properties.read('./config/restConfig.ini')
        if env == 'T':
            props = properties["TEST"]
        else:
            props = properties["PROD"]
        return props

    def send_api(self, path, method):
        API_HOST = self.props["api_host"]
        url = API_HOST + path
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        body = {"key1": "value1", "key2": "value2"}

        try:
            if method == 'GET':
                response = requests.get(url, headers)
            elif method == 'POST':
                response = requests.put(url, headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
            print("response status %r" % response.status_code)
            print("response status %r" % response.status_code)
        except Exception as ex:
            print(ex)

## send_api("/test", "POST")

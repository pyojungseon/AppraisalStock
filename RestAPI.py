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

    def send_api(self, path, method, userData):
        API_HOST = self.props["api_host"]
        url = API_HOST + path
        # headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
        body = {userData[0]:userData[1], userData[2]:userData[3]}

        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url, json=body)
            elif method == 'PUT':
                response = requests.put(url, json=body)
            elif method == 'DELETE':
                response = requests.delete(url, json=body)

            print("response status %r" % response.status_code)
            print("response data %r" % response.text)

        except Exception as ex:
            print(ex)

## send_api("/test", "POST")

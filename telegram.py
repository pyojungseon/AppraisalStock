from rabbitMQ.msgQPublisher import MsgQPublisher
import time
import configparser

class Telegram:

    env = None
    msgQ = None

    def __init__(self, _env):
        print("Notice Constructor : %s" % _env)
        self.env=_env
        self.msgQ = MsgQPublisher()

    def __del__(self):
        print("Notice Destructor")
    
    def getConfig(self, env):
        properties = configparser.ConfigParser()
        properties.read('./config/config.ini')
        if env=='T':
            props = properties["TEST"]
        else:
            props = properties["PROD"]
        print("Mode : %s" % props["env"])
        return props

    def sendData(self, data):
        msg = self.env+"||"+"2026330004"+"||["+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))+"]"+data
        print(msg)
        self.msgQ.send(msg)

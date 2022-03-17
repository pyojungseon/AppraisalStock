from TelegramBot import TelegramBot
from DataReader import DataReader
import time


class TelegramCommand:
    _env = ''
    tg = ''
    dr = ''

    def __init__(self, _env):
        print('init telegramBot command')

        self._env = _env

        # init telegram chatbot
        self.tg = TelegramBot(_env)

        # init Data Reader
        self.dr = DataReader()

    def getPrice(self, update, context):
        reqData = update.message.text.split(" ")
        companyCode = reqData[1]
        fromDate = str(int(time.strftime('%Y%m%d', time.localtime(time.time()))) - 1)
        toDate = time.strftime('%Y%m%d', time.localtime(time.time()))
        value = self.dr.getStockData(companyCode, fromDate, toDate)
        text = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + \
               "\n시가 : " + str(value.tail(1).to_numpy()[0, 0]) + \
               "\n하한가 : " + str(value.tail(1).to_numpy()[0, 1]) + \
               "\n상한가 : " + str(value.tail(1).to_numpy()[0, 2]) + \
               "\n종가 : " + str(value.tail(1).to_numpy()[0, 3])
        msg = self._env + "||" + str(update.effective_chat.id) + "||" + text
        print(msg)
        self.tg.sendMsg(msg)

    def start(self, update, context):
        text = "[AppraisalStock] " + ". 사용법을 알고싶으시면 /help를 입력하여주세요"
        msg = self._env + "||" + str(update.effective_chat.id) + "||" + text
        print(msg)
        self.tg.sendMsg(msg)

    def help(self, update, context):
        text = '''/get : 주가 정보
                \n개발중.'''
        msg = self._env + "||" + str(update.effective_chat.id) + "||" + text
        print(msg)
        self.tg.sendMsg(msg)

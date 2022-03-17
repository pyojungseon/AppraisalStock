from TelegramBot import TelegramBot


class TelegramCommand:

    _env = ''
    tg = ''

    def __init__(self, _env):
        print('init telegramBot command')

        self._env = _env

        # init telegram chatbot
        self.tg = TelegramBot(_env)

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

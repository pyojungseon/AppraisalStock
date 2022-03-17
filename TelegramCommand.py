from TelegramBot import TelegramBot

_env = ''
tg = ''


class TelegramCommand:

    def __init__(self, _env):
        self._env = _env

        # init telegram chatbot
        self.tg = TelegramBot(_env)

    def start(self, update, context):
        env_name = ''
        if _env == 'T':
            env_name = '[TEST]'
        text = "[AppraisalStock] " + env_name + ". 사용법을 알고싶으시면 /help를 입력하여주세요"
        msg = _env + "||" + str(update.effective_chat.id) + "||" + text
        tg.sendData(msg)

    def help(self, update, context):
        text = '''/get : 주가 정보
                \n개발중.'''
        msg = _env + "||" + str(update.effective_chat.id) + "||" + text
        tg.sendData(msg)

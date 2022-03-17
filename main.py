from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from TelegramCommand import TelegramCommand
import configparser
import sys


def getConfig(_env):
    properties = configparser.ConfigParser()
    properties.read('./config/config.ini')
    if _env == 'T':
        props = properties["TEST"]
    else:
        props = properties["PROD"]
    print("Mode : %s" % props["env"])
    return props


_env = 'T'

# _env setting. Prod / Test
if len(sys.argv) < 2:
    print("Arguments missing")
    sys.exit()
elif sys.argv[1] != 'P' and sys.argv[1] != 'T':
    print("Check Arguments : [P]/[T]")
    sys.exit()
else :
    env = sys.argv[1]


# set properties
props = getConfig(_env)


# set telegram command
updater = Updater(token=props["token"], use_context=True)
dispatcher = updater.dispatcher

tc = TelegramCommand(_env)

start_handler = CommandHandler('start', tc.start())
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', tc.help())
dispatcher.add_handler(help_handler)

updater.start_polling()
updater.idle()
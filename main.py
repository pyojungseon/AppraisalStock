from DataReader import DataReader
from telegram import Telegram

df = DataReader()
data = df.getStockData()

tg = Telegram()
tg.sendData("test")
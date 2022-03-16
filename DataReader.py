# https://github.com/FinanceData/FinanceDataReader/wiki/
# pip install finance-datareader

import FinanceDataReader as fdr

class DataReader:

    def __init__(self):
        print('DataReader class init')

    def getStockData(self):
        # Apple(AAPL), 2017-01-01 ~ Now
        df = fdr.DataReader('AAPL', '2017')
        print(df)
        return df

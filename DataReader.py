# https://github.com/FinanceData/FinanceDataReader/wiki/
# pip install finance-datareader
import FinanceDataReader as fdr


class DataReader:

    def __init__(self):
        print('DataReader class init')

    def getStockData(self, companyCode, fromDate, toDate):
        df = fdr.DataReader(companyCode, fromDate, toDate)
        print(df)
        return df

import yfinance as yf
import pandas_datareader.data as web
import datetime
from matplotlib import pyplot as plt
#from matplotlib import dates as mdates

yf.pdr_override()

start=datetime.datetime(2021, 1, 1)
end=datetime.datetime.today()

ethereum=web.get_data_yahoo('ETH-USD',start,end)
bitcoin=web.get_data_yahoo('BTC-USD',start,end)
ada=web.get_data_yahoo('ADA-USD',start,end)
solana=web.get_data_yahoo('SOL1-USD',start,end)

#days= mdates.drange(start,end,datetime.timedelta(days=1))
#import pandas as pd

#stocks = pd.DataFrame({ "AAPL": apple["Adj Close"],
#                          "MSFT": microsoft["Adj Close"],
#                          "GOOG": google["Adj Close"]})   

# stocks.plot(grid = True)
# stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True)
# stocks.show()

plt.plot(ethereum)
plt.show()
# plt.plot(bitcoin)
# plt.show()
# plt.plot(ada)
# plt.show()
# plt.plot(solana)
# plt.show()
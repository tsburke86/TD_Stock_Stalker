import os
from Func import *
from Stock import *
from Portfolio import *
from Trade import *

# Set trade files and make the portfolio
setTotalTrades()
holdings = os.path.abspath('holdings.csv')
transactions = os.path.abspath('total.csv')
h = makeHoldingDict(holdings)
t = makeTradeList(transactions)
port = Portfolio(t, h)

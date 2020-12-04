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

a = port.getStock('AAPL')
'''
print(a.getBlocks())
print(a.getBlock(0).getBlockProfit())
print(a.getBlock(1).getBlockProfit())
print()
'''

def printBlocks(port, ticker):
    counter = 1
    for i in port.getStock(ticker).getBlocks(): # i is the block
        print('--| Block #'+str(counter)+"  "+i.getDates()+' |--')
        #print('Profit: ${:.2f}'.format(i.getProfit()))
        print('Block Profit: ${:.2f}'.format(i.getBlockProfit())+'\n')
        i.printTrades()
        shortBreak()
        counter += 1
printBlocks(port, 'AAPL')

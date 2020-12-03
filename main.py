from Func import *
#from Stock import *
from Portfolio import *
from Trade import *



holdings = 'C:/Users/Tim/PycharmProjects/pythonProject/holdings.csv'
transactions = 'C:/Users/Tim/PycharmProjects/pythonProject/total.csv'

h = makeHoldingDict(holdings)
t = makeTradeList(transactions)
port = Portfolio(t, h)
#port.getStock('AAPL').printTrades()
#port.printStocks()
#port.getStock('MRVL').getProfit()
#print(port.getStock('MRVL'))
#for i in port.getTradeList(): print(i)
print("\n## ALL TRADES ##\n");
for i in range(len(port.getGainers())): print(port.getGainers()[i])
print("#########\n")
print("\n## GAINERS ##\n");
for i in range(4): print(port.getGainers()[i])
print("#########\n")
print("\n## LOSERS ##\n");
               
for i in range(4):
    try: print(port.getLosers()[i])
    except IndexError: break
print("#########\n")
print("\n## MOST INVESTED ##\n");
for i in range(6):
    try: print(port.getInvested()[i])
    except IndexError: break
print("#########\n")
print("Total Profit: ${:.2f}".format(port.getTotalProfit()))
print("Total Invested: ${:.2f}".format(port.getTotalInvested()))
#print(one[0].getTicker())
#print(one[0].getEquity())
'''
print("\t###\nHoldings")
for key,value in h.items(): print(value)
print("\t###\nTransactions")
for i in t: print(i)
'''

'''
tradeList = makeTradeList(filename)
port = Portfolio(tradeList)
port.printStocks()
'''


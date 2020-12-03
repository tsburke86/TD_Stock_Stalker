from Func import *
#from Stock import *
from Portfolio import *
from Trade import *


def main():
    import os
    # Set trade files and make the portfolio
    setTotalTrades()
    holdings = os.path.abspath('holdings.csv')
    transactions = os.path.abspath('total.csv')
    h = makeHoldingDict(holdings)
    t = makeTradeList(transactions)
    port = Portfolio(t, h)
    
    while True:
        print()
        print("\t########################")
        print("\t## TD ALL TRADES MENU ##")
        print("\t########################")
        print(" --------------------------------")
        print("| 1\t| Print All Stocks Info  |")
        print("| 2\t| Print Top 5 Gainers    |")
        print("| 3\t| Print Top 5 Losers     |")
        print("| 4\t| Print Top 6 Invested   |")
        print("| q\t| Quit                   |")
        print(" --------------------------------")
        # Basic Stats
        printStats(port)
        print()
        entry = input("Enter the option from above: ")
        lineBreak()
        if entry.upper() == 'Q': break
        elif entry == '1': printAllTrades(port)
        elif entry == '2': printGainers(port)
        elif entry == '3': printLosers(port)
        elif entry == '4': printInvested(port)
        else: print("Bad Entry")
        lineBreak()
    print()
    print("Until Next Time...")
    print()
        


main()
#printGainers(port)
#printStats(port)
#port.getStock('AAPL').printTrades()
#port.printStocks()
#port.getStock('MRVL').getProfit()
#print(port.getStock('MRVL'))
#for i in port.getTradeList(): print(i)

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


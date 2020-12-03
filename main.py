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
        print()
        # Basic Stats
        printStats(port)
        print()
        print(" --------------------------------")
        print("| 1\t| Print All Stocks Info  |")
        print("| 2\t| Print Top 5 Gainers    |")
        print("| 3\t| Print Top 5 Losers     |")
        print("| 4\t| Print Top 6 Invested   |")
        print("| q\t| Quit                   |")
        print(" --------------------------------")
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
    print()

main()

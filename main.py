from Func import *
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
        # Basic Stats
        printStats(port)
        printTickers(port)
        print()
        print("    ###########################")
        print("    ## TD STOCK STALKER MENU ##")
        print("    ###########################")
        print("/--------------------------------\\")
        print("| 1\t| Print All Stocks Info  |")
        print("| 2\t| Print Top 5 Gainers    |")
        print("| 3\t| Print Top 5 Losers     |")
        print("| 4\t| Print Top 6 Invested   |")
        print("| q\t| Quit                   |")
        print("| Enter the ticker for trades    |")
        print("\\--------------------------------/")
        print()
        entry = input("Enter the option from above: ")
        lineBreak()
        if entry == 'q': break
        elif entry.upper() in port.getStocks():
            printBlocks(port, entry.upper())
            print("Stock Info:")
            print(port.getStock(entry.upper()))
        elif entry == '1': printAllTrades(port)
        elif entry == '2': printGainers(port)
        elif entry == '3': printLosers(port)
        elif entry == '4': printInvested(port)
        else: print("Bad Entry")
        lineBreak()
        cont = input("PRESS ENTER TO CONTINUE")
        cont = None
        print()
        print()
    print()
    print("Until Next Time...")
    print()
    print()

main()

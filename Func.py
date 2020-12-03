from Trade import *
### Functions for printing ###
def printAllTrades(port):
    print("\n\t## ALL TRADES ##\n")
    for i in range(len(port.getGainers())): print(port.getGainers()[i])
    print()
    
def printGainers(port, amount=5):
    print("\t#############")
    print("\t## GAINERS ##")
    print("\t#############\n")
    for i in range(amount): print(port.getGainers()[i])
    print()
    
def printLosers(port, amount=5):
    print("\t############")
    print("\t## LOSERS ##")
    print("\t############\n")
    if len(port.getLosers()) == 0:
        return "Wow, no negative stocks!"
    for i in range(amount):
        try: print(port.getLosers()[i])
        except IndexError: break
    print()

def printInvested(port, amount=6):
    print("\t###################")
    print("\t## MOST INVESTED ##")
    print("\t###################\n")
    for i in range(amount):
        try: print(port.getInvested()[i])
        except IndexError: break
    print()
def printStats(port):
    print("  --Basic Stats--")
    print("Total Profit: ${:.2f}".format(port.getTotalProfit()))
    print("Total Secured Profit: ${:.2f}".format(port.getTotalSecuredProfit()))
    print("Total Invested: ${:.2f}".format(port.getTotalInvested()))

def lineBreak():
    print("\n------------------------------------------")
#########################

    
def setTotalTrades():
    import os
    import glob
    # the path to your csv file directory
    pathToDir = os.path.abspath('TradesFiles')
    csvdir = pathToDir+'\\*.csv'

    fileList = glob.glob(csvdir)
    total = open('total.csv', 'w')
    for file in fileList:
        openFile = open(file,'r')
        for line in openFile.readlines():
            total.write(line)
        openFile.close()
    total.close()


def makeTradeList(file):
    tradeList = []
    import csv
    with open(file, 'r') as data:
        next(data)
        for line in csv.reader(data):
            if len(line) < 3: continue
            if 'Bought' in line[2] or 'Sold' in line[2]:
                trade = Trade(line)
                tradeList.append(trade)
    return tradeList

def makeHoldingDict(file):
    holdingDict = {}
    import csv
    with open(file, 'r') as data:
        for i in range(4): next(data)
        for line in csv.reader(data):
            if line == []: break
            if len(line[0]) > 5: continue
            #print(line)

            holding = Holding(line)
            holdingDict[line[0]] = holding

    return holdingDict

### Probably not in use

def printStocks(sList, amount):
    for i in range(amount):
        print(sList[i])


def printProfit(stock):
    for i in stock.getTradeList():
        trade = i.getType()
        total = i.getTotal()
        if trade == 'buy':
            buys += total
        else:
            sells += total
    print("The total money invested is: ${:.2f}".format(buys))
    print("The total money sold is:     ${:.2f}".format(sells))
    print("Currently Invested:          ${:.2f}".format(currentHolding))
    print("The total profit is:         ${:.2f}".format(sells - buys \
                                                        + currentHolding))

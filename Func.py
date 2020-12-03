from Trade import *

def setTotalTrades(pathToDir):
    import glob
    # the path to your csv file directory
    # 'C:\\Users\\Tim\\PycharmProjects\\pythonProject\\Trades\\'
    csvdir = pathToDir+'*'

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

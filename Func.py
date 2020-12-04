from Trade import *
### Functions for printing with portfolios ###
def printAllTrades(port):
    print("\t################")
    print("\t## ALL STOCKS ##")
    print("\t################\n")
    for i in range(len(port.getGainers())):
        print(port.getGainers()[i]); shortBreak()
    print()
    
def printGainers(port, amount=5):
    print("\t#############")
    print("\t## GAINERS ##")
    print("\t#############\n")
    for i in range(amount): print(port.getGainers()[i]); shortBreak()
    print()
    
def printLosers(port, amount=5):
    print("\t############")
    print("\t## LOSERS ##")
    print("\t############\n")
    if len(port.getLosers()) == 0:
        return "Wow, no negative stocks!"
    for i in range(amount):
        try: print(port.getLosers()[i]); shortBreak()
        except IndexError: break
    print()

def printInvested(port, amount=6):
    print("\t###################")
    print("\t## MOST INVESTED ##")
    print("\t###################\n")
    for i in range(amount):
        try: print(port.getInvested()[i]); shortBreak()
        except IndexError: break
    print()
    
def printStats(port):
    print("  --Basic Account Stats--")
    print("Total Profit: ${:.2f}".format(port.getTotalProfit()))
    print("Total Secured Profit: ${:.2f}".format(port.getTotalSecuredProfit()))
    print("Total Invested: ${:.2f}".format(port.getTotalInvested()))

def lineBreak():
    print("|---------------------------------------------------|\n")

def shortBreak():
    print("---------------\n")
    
#########################

# Dealing with the files
    
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

##################

# Print the Blocks nicely
def printBlocks(port, ticker):
    counter = 1
    for i in port.getStock(ticker).getBlocks(): # i is the block
        print('--| Block #'+str(counter)+"  "+i.getDates()+' |--')
        #print('Profit: ${:.2f}'.format(i.getProfit()))
        print('Block Profit: ${:.2f}'.format(i.getBlockProfit())+'\n')
        i.printTrades()
        shortBreak()
        counter += 1


# Print all trades for a stock
def printTrades(port, ticker):
        print()
        print(port.getStock(ticker))
        print()
        print("## TRADES ##")
        print()
        port.getStock(ticker).printTrades()
        print()
        null = input("PRESS ENTER TO CONTINUE")

# Print tickers of held shares
def printTickers(port, width=5):
    print()
    print("  TICKERS TRADED")
    counter = 1
    for key,value in port.getStocks().items():
        print(value.getTicker(),end='\t')
        counter += 1
        if counter > width:
            counter = 1
            print()




### Probably not in use

def printStocks(sList, amount):
    for i in range(amount):
        print(sList[i])


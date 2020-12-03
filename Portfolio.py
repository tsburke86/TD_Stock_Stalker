from Stock import *

# Function to sort the profit list
def getProfit(stock):
    return stock.getProfit()
def getInvested(stock):
    return stock.getInvested()

class Portfolio():

    def __init__(self, tradeList, holdingsDict):
        self.__stocks = {}   # ticker: Stock()
        self.__holdingsDict = holdingsDict
        self.__tradeList = tradeList
        self.__gainers = []
        self.__losers = []
        self.__highestInvested = []
        self.__totalProfit = 0
        self.__totalSecuredProfit = 0
        self.__totalInvested = 0
        self.setStocks(tradeList)
        self.setTotalProfit()
        self.setStockTotalProfit()
        self.setGainers()
        self.setLosers()
        self.setInvested()

    # Getters
    def getStock(self, entry):
        return self.__stocks[entry]
    def getStocks(self):
        return self.__stocks
    def getHoldings(self):
        return self.__holdingsDict
    def getTotalProfit(self):
        return self.__totalProfit
    def getTotalSecuredProfit(self):
        return self.__totalSecuredProfit
    def getTradeList(self):
        return self.__tradeList
    def getGainers(self):
        return self.__gainers
    def getLosers(self):
        return self.__losers
    def getInvested(self):
        return self.__highestInvested
    def getTotalInvested(self):
        return self.__totalInvested


    # Setters
    def setTotalProfit(self):  # Sets totalProfit and totalInvested
        tp = 0  # Total Profit
        ti = 0  # Total Invested
        tsp = 0 # Total Secured Profit (Actually Traded)
        for key,value in self.__stocks.items():
            tp += value.getProfit()
            ti += value.getInvested()
            tsp += value.getSecuredProfit()
        self.__totalProfit = tp
        self.__totalInvested = ti
        self.__totalSecuredProfit = tsp
        
    def setStockTotalProfit(self):
        tp = self.__totalProfit
        ti = self.__totalInvested
        for key,value in self.__stocks.items():
            value.setTotalProfit(tp)
            value.setTotalInvested(ti)
        
    def setGainers(self):
        gainers = []
        for key,value in self.__stocks.items():
            gainers.append(value)
        gainers.sort(key=getProfit,reverse=True)
        self.__gainers = gainers
        

    
    def setInvested(self):
        invested = []
        for key,value in self.__stocks.items():
            invested.append(value)
        invested.sort(key=getInvested,reverse=True)
        self.__highestInvested= invested


    def setLosers(self):
        losers = []
        limit = 0
        for key,value in self.__stocks.items():
            if value.getProfit() < limit:
                losers.append(value)
        losers.sort(key=getProfit)
        self.__losers = losers



    def setStocks(self, tradeList):
        ticker = ''
        for trade in tradeList:
            ticker = trade.getTicker();
            if ticker not in self.__stocks:
                stock = Stock(ticker,self.__holdingsDict)
                self.__stocks.update({ticker:stock})
            self.__stocks[ticker].appendTrade(trade)

        for key,value in self.__stocks.items():
            value.setProfit()

    # Misc
    def printStocks(self):
        for key,value in self.__stocks.items():
            print(value)


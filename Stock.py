'''
The Stock Object is a list containing all the trade objects for that ticker.
It takes in the holdings as a dictionary (hDict) and quereys the stocks ticker
to see if you currently have a position.


'''

class Stock():
    def __init__(self, ticker, hDict):
        self.__tradeList = []       # All trades
        self.__ticker = ticker
        self.__profit = 0
        self.__shares = 0
        self.__holding = 0
        self.__AVC = 0
        self.__mark = 0
        self.__totalProfit = 0
        self.__profitPercent = 0
        self.__investedPercent = 0
        self.__percentChg = 0
        self.__heldProfit = 0        # Profit from shares currently held
        self.__securedProfit = 0     # Profit secured by selling shares
        self.setHolding(hDict)
        
    def __str__(self):
        return self.__ticker+"\tShares Held: {:.0f}".format(self.__shares)\
                +"  \t% Chg: {:.2f}".format(self.__percentChg)+'%'\
               +"\n\tPosition: ${:.2f}".format(self.__AVC)\
                +"  \tCurrent: ${:.2f}".format(self.__mark)\
               +"\n\tInvested: ${:.2f}".format(self.__AVC * self.__shares)\
               +"  \tImpact: "+self.getInvestedPercent()+"%"\
               +"\n\tTotal $$$: ${:.2f}".format(self.__profit)\
               +"  \tImpact: "+self.getProfitPercent()+"%"\
               +"\n\t$$$ Secured: ${:.2f}".format(self.__securedProfit)\
               +"\t$$$ from Shares: ${:.2f}".format(self.__heldProfit)+'\n'

    def getTicker(self):
        return self.__ticker
    def getInvested(self):
        return self.__AVC * self.__shares
    def getShares(self):
        return self.__shares
    def getTradeList(self):
        return self.__tradeList
    def getProfit(self):
        return self.__profit
    def getTotalProfit(self):
        return self.__totalProfit
    def getProfitPercent(self):
        return format(self.__profitPercent, '.2f')
    def getInvestedPercent(self):
        return format(self.__investedPercent, '.2f')
    def getHolding(self):
        return self.__holding
    def getAVC(self):
        return self.__AVC

    # Setters

    def setHolding(self,hDict):
        if self.__ticker in hDict:
            self.__holding = hDict[self.__ticker]
            self.__mark = self.__holding.getMark()


    def setProfit(self):
        hStock = self.__holding
        shares = 0
        AVC = 0
        ticker = self.__ticker
        if hStock != 0:
            shares = hStock.getQuantity()
            AVC = hStock.getPrice()
            currentEquity = hStock.getEquity()
            currentHolding = shares * AVC
        else: currentHolding = 0; currentEquity = 0

        buys = 0
        sells = 0
        for i in self.__tradeList:
            trade = i.getType()
            total = abs(i.getTotal())
            if trade == 'Buy':
                buys += total
            else: sells += total
        self.__heldProfit = currentEquity - currentHolding
        self.__securedProfit = sells - buys + currentHolding 
        self.__profit = self.__securedProfit + self.__heldProfit
        self.__shares = shares
        self.__AVC = AVC
        
    def setTotalProfit(self, tp):
        self.__totalProfit = tp
        self.__profitPercent = self.__profit / tp * 100
        
    def setTotalInvested(self, ti):
        self.__totalInvested = ti
        if ti != 0:
            self.__investedPercent = self.getInvested() / ti * 100
        if self.__mark != 0:
            self.__percentChg = self.__AVC / self.__mark

    def appendTrade(self, trade):
        self.__tradeList.append(trade)

    def printTrades(self):
        for i in self.__tradeList:
            print(i)

    def callTrade(self, i):
        return self.__tradeList[i]

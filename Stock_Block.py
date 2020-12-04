from Func import *
from Block import *

'''
The Stock Object is a list containing all the trade objects for that ticker.
It takes in the holdings as a dictionary (hDict) and quereys the stocks ticker
to see if you currently have a position.


'''

class Stock():
    def __init__(self, ticker, hDict):
        self.__tradeList = []       # All trades
        self.__ticker = ticker
        self.__profit = 0           # Profit from held shares and trades
        self.__shares = 0
        self.__holding = 0
        self.__AVC = 0              # Current position
        self.__mark = 0             # Current trading price                
        self.__totalProfit = 0      # Total Profit from the porifolio
        self.__profitPercent = 0
        self.__investedPercent = 0
        self.__percentChg = 0
        self.__heldProfit = 0        # Profit from shares currently held
        self.__securedProfit = 0     # Profit secured by selling shares
        self.setHolding(hDict)

        # Block Stuff
        self.__blockList = []
        
    def __str__(self):
        long = " "+self.__ticker+"\tDate Range: "+self.getDates()\
               +"\n\tShares Held: {:.0f}".format(self.__shares)\
               +"  \t% Gain: {:.2f}".format(self.getCurrentPercent())+"%"\
               +"\n\tPosition: ${:.2f}".format(self.__AVC)\
               +"  \tCurrent: ${:.2f}".format(self.__mark)\
               +"\n\tInvested: ${:.2f}".format(self.__AVC * self.__shares)\
               +"  \tImpact: "+self.getInvestedPercent()+"%"\
               +"\n\tTotal $$$: ${:.2f}".format(self.__profit)\
               +"  \tImpact: "+self.getProfitPercent()+"%"\
               +"\n\t$$$ Secured: ${:.2f}".format(self.__securedProfit)\
               +"\t$$$ from Shares: ${:.2f}".format(self.__heldProfit)
        
        short = " "+self.__ticker+"\tDate Range: "+self.getDates()\
                +"\n\t$$$ Secured: ${:.2f}".format(self.__securedProfit)\
                +"  \tImpact: "+self.getProfitPercent()+"%"
                
        if self.__mark == 0: return short
        else: return long

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
    def getSecuredProfit(self):
        return self.__securedProfit
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
    def getCurrentPercent(self):
        if self.__mark != 0:
            return (self.__mark - self.__AVC) / self.__AVC * 100
        else: return 0
        
    def getDates(self):
        start = self.__tradeList[0].getDate()
        if self.__AVC == 0: last = self.__tradeList[-1].getDate()
        else: last = "present"
        return start+" - "+last

    # Blocks
    def getBlock(self, i):
        return self.__blockList[i]
    
    def getBlocks(self):
        return self.__blockList

    def getBlockListLength(self):
        return len(self.__blockList)
    

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

    def setBlocks(self):
        buys = 0
        sells = 0
        shares = 0
        # avcShares is for generating the average cost for the block
        avcShares = 0

        blockProfit = 0 # For the entire block
        
        for i in range(len(self.__tradeList)):
            profit = 0 # For each trade, reset each time

            if shares == 0:
                block = Block()
                self.__blockList.append(block)
                blockProfit = 0
                buys = 0
                sells = 0
                shares = 0
                avcShares = 0
            
            trade = self.__tradeList[i]
            if trade.getType() == 'Buy':
                buys += abs(trade.getTotal())
                shares += trade.getQuantity()
                avcShares += trade.getQuantity()
                avc = buys / avcShares
                trade.setAVC(avc)
            else:
                trade.setAVC(avc)
                sells += trade.getTotal()
                shares -= trade.getQuantity()
                profit = trade.getTotal() - \
                         trade.getAVC() * trade.getQuantity()
                blockProfit += profit
                
                
            if shares == 0: holding = 0
            else: holding = buys - sells
            
            trade.setHeldShares(shares)
            trade.setHolding(holding)
            trade.setAVC(avc)
            trade.setProfit(profit)
            block.append(trade)
            block.setStats(buys,sells,shares,avcShares,blockProfit)
        
            

    def appendTrade(self, trade):
        self.__tradeList.append(trade)

    def printTrades(self):
        for i in self.__tradeList:
            print(i)
            shortBreak()

    def callTrade(self, i):
        return self.__tradeList[i]

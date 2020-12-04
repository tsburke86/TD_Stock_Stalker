from Func import *
class Block():
    def __init__(self):
        self.__blockList = []
        self.__blockHolding = []
        self.__sellTotal = 0
        self.__buyTotal = 0
        self.__profit = 0
        self.__blockProfit = 0
        self.__currentProfit = 0
        self.__averageCost = 0
        self.__currentShares = 0

    # Getters        
    def getBlockList(self):
        return self.__blockList
    def getBlockProfit(self):
        return self.__blockProfit
    def getLength(self):
        return len(self.__blockList)
    def getSellTotal(self):
        return self.__sellTotal
    def getBuyTotal(self):
        return self.__buyTotal
    def getCurrentProfit(self):
        return self.__currentProfit
    def getAVC(self):
        return self.__averageCost
    def getCurrentShares(self):
        return self.__currentShares
    def getProfit(self):
        return self.__profit
    def getDates(self):
        start = self.__blockList[0].getDate()
        if self.__blockList[-1].getHeldShares() == 0:
            last = self.__blockList[-1].getDate()
        else: last = "Present"
        return start+" - "+last
    def printTrades(self):
        for i in self.__blockList:
            print(i.printTrade())

    # Setters
    def setStats(self,buys,sells,shares,avcShares,blockProfit):
        self.__blockProfit = blockProfit
        self.__sellTotal = sells
        self.__buyTotal = buys
        self.__currentShares = shares
        self.__profit = sells - buys
        self.__averageCost = buys / avcShares
        self.__currentProfit = self.__profit + shares * self.__averageCost
        
    def append(self, trade):
        self.__blockList.append(trade)

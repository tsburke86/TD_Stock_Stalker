'''
TD Transactions file
0'DATE'
1'TRANSACTION ID'
2'DESCRIPTION'
3'QUANTITY'
4'SYMBOL'
5'PRICE'
6'COMMISSION'
7'AMOUNT'
8'REG FEE'
9'SHORT-TERM RDM FEE'
10'FUND REDEMPTION FEE'
11' DEFERRED SALES CHARGE']


'''


class Trade():
    def __init__(self, i):
        self.__ticker = i[4]
        self.__description = i[2]
        self.__date = i[0]
        self.__quantity = i[3]
        self.__price = i[5]
        self.__type = str()
        self.__total = i[7]
        # variable attributes
        self.setType()
        self.__averageCost = 0
        self.__profit = 0

    def __str__(self):
        return self.__date + " " + self.__description+\
    " for a total of: $"+self.__total
    # Getters
    def getTicker(self):
        return self.__ticker

    def getDescription(self):
        return self.__description

    def getDate(self):
        return self.__date

    def getQuantity(self):
        return eval(self.__quantity)

    def getPrice(self):
        return eval(self.__price)

    def getType(self):
        return self.__type

    def getTotal(self):
        return eval(self.__total)

    def getAverageCost(self):
        return self.__averageCost

    def getProfit(self):
        return self.__profit

    # Setters
    def setAverageCost(self, cost):
        self.__averageCost = cost

    def setProfit(self, profit):
        self.__profit = profit

    def setQuantity(self, q):
        self.__quantity = q

    def setTotal(self):
        self.__total = self.__quantity * self.__price

    def setType(self):
        if 'Bought' in self.__description:
            self.__type = 'Buy'
        else: self.__type = "Sell"

    def reduceQuantity(self):
        self.__quantity -= 1

# A holding object is like a trade object.  There is one for each stock you have.
'''
TD Holdings file
0 Instrument, 1 Qty, 2 Trade Price, 3 Mark, Net Liq, Mrk Chng, Days,P/L %,P/L YTD,P/L Open,P/L Day,BP Effect
AAPL, +5, 109.03, 122.36, $611.80, +3.31, ,+11.76%,$64.15,$64.39,$16.55,$428.26

'''
class Holding():
    def __init__(self, hList):
        self.__ticker = hList[0]
        self.__quantity = int(hList[1])
        self.__price = float(hList[2])
        self.__mark = float(hList[3])
        self.__equity = float(hList[3])*float(hList[1])

    def __str__(self):
        v = self.__ticker + ' - Equity: $' + str(format(self.__equity,'.2f')) +\
            " Shares: " + str(self.__quantity) + " Price: $" + str(format(self.__equity,'.2f'))
        return v

    def getTicker(self):
        return self.__ticker

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price
    def getMark(self):
        return self.__mark

    def getEquity(self):
        return self.__equity




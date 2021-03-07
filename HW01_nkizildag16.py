from random import uniform


class investments_tools:               # to make easier creating new tools
    def __init__(self, price, name):
        self.price = price
        self.name = name


class Stock(investments_tools):
    def __init__(self, price, name):
        super().__init__(price, name)  # to construct same fields super is used


class MutualFund(investments_tools):
    def __init__(self, name):
        super().__init__(1, name)


class Bond(investments_tools):                        #bond is created. it works similar to the other investment tools
    def __init__(self, price, name):                  #I assume that is uniformly drawn from [0.7-1.7]
        super().__init__(price, name)


class Portfolio:
    def __init__(self):
        self.balance = 0
        self.investment_dict = {}  # initialize empty dictionary to store investment tools
        self.transactions = []     #to print history
        self.transactions.append("Dear Madam/Sir, Welcome to the Portfolio software")

    def is_investment_in_dict(self, investment_name):
        for key in self.investment_dict:
            if investment_name == key.name:
                return True
        return False

    def get_investment(self, investment_name):
        for key in self.investment_dict:
            if investment_name == key.name:
                return key
        return None

    def addCash(self, addCash):
        if addCash < 0:
            self.transactions.append("Negative value is not accepted")
        else:

            self.balance += addCash
            self.transactions.append("AddCash is = " + str(addCash) + " New balance is = " + str(self.balance))

    def withdrawCash(self, withdrawCash):
        if self.balance >= withdrawCash:
            self.balance -= withdrawCash
            self.transactions.append("You Withdrew:" + str(withdrawCash) + " New balance is = " + str(self.balance))
            return True
        else:
            self.transactions.append("Insufficient balance  ")
            return False

    def buy_investment(self, share, investment, tip):
        total_price = share * investment.price
        if self.withdrawCash(total_price):
            if investment in self.investment_dict:
                self.investment_dict[investment] += share
            else:
                self.investment_dict[investment] = share
            self.transactions.append("Bought " + tip + ": " + investment.name + " share: " + str(share))
        else:
            self.transactions.append("Cannot buy " + tip + ": " + investment.name + " share: " + str(share))

    def buyStock(self, share: int, stock: Stock):
        self.buy_investment(share, stock, "stock")

    def buyMutualFund(self, share: float, mt: MutualFund):
        self.buy_investment(share, mt, "mutual fund")
    def buyBond(self,share:int,bond: Bond):
        self.buy_investment(share,bond, "bond")

    def sell_investment(self, investment_name, share, tip, coef):
        if not self.is_investment_in_dict(investment_name):
            self.transactions.append("You have not that" + tip)
        else:
            investment = self.get_investment(investment_name)
            if share > self.investment_dict[investment]:
                self.transactions.append("Cannot buy due to insufficient " + tip)
            else:
                total_gain = share * coef * investment.price
                self.addCash(total_gain)
                self.investment_dict[investment] -= share
                self.transactions.append("Congrats' You sold!!" + tip + ": " + investment.name)

    def sellStock(self, stock_name: str, share: int):
        self.sell_investment(stock_name, share, "stock", uniform(0.5, 1.5))

    def sellMutualFund(self, mt_name, share: float):
        self.sell_investment(mt_name, share, "mutual fund", uniform(0.9, 1.2))

    def sellBond(self, bond_name, share: int):
        self.sell_investment(bond_name, share, "bond", uniform(0.7, 1.7))

    def history(self):                       # to see in separate lines
        for transaction in self.transactions:
            print(transaction)

    def history2(self):                     # to see in one line
        print(self.transactions)


portfolio = Portfolio()  # Creates a new portfolio
portfolio.addCash(300.50)  # Adds cash to the portfolio
s = Stock(20, "HFH")  # Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s)  # Buys 5 shares of stock s
mf1 = MutualFund("BRT")  # Create MF with symbol "BRT"
mf2 = MutualFund("GHT")  # Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1)  # Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2)  # Buys 2 shares of "GHT"
portfolio.sellMutualFund("BRT", 3)  # Sells 3 shares of BRT
portfolio.sellStock("HFH", 1)  # Sells 1 share of HFH
b = Bond(30, "ZRT")  #Create Bond with price 100 and symbol "ZRT"
portfolio.buyBond(1, b)
portfolio.sellBond("ZRT", 1)
portfolio.withdrawCash(50)  # Removes $50
portfolio.history()  # Prints a list of all transactions  ordered by time


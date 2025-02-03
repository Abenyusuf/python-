class Creditcard:
    def get_Customer(self):
        pass


class CreditCard:
    """"A consumer credit card class."""

    def __init__(self, Customer, Bank, Account, Limit, ):
        # Create Private Member Variables
        self._Customer = Customer
        self._Bank = Bank
        self._Account = Account
        self._Balance = 0
        self._Limit = Limit

    def get_Customer(self):
        """Return The Name Of The Customer"""
        return self._Customer

    def get_Bank(self):
        """Return The Name Of The Bank"""
        return self._Bank

    def get_Account(self):
        """Return The Account """
        return self._Account

    def get_Limit(self):
        """Return The Limit"""
        return self._Limit

    def get_Balance(self):
        """Return The Limit"""
        return self._Balance

    def Charge(self, Price):
        """Return The balance after the charge"""
        if (Price + self._Balance) > self._Limit:
            return False
        else:
            New_Balance = self._Balance + Price
            self._Balance = New_Balance
            return self._Balance

    def Make_Payment(self, Amount):
        self._Balance = self._Balance - Amount


BoaCreditCard = CreditCard('Jane Doe', 'Bank of America', 552211, 1000, )
BoaCreditCard.Charge(500)
print(BoaCreditCard.get_Customer())
print('Balance =', BoaCreditCard.get_Balance())
BoaCreditCard.Make_Payment(300)
print('Balance after payment =', BoaCreditCard.get_Balance())


jcpCreditCard = CreditCard('John Doe', 'JCpenny', 879966, 500)

print(jcpCreditCard.get_Bank())

from CreditCard import Creditcard, CreditCard


class PredatoryCreditCard(Creditcard, CreditCard):
    pass

    def __init__(self, Customer, Bank, Account, Limit, ):
        super().__init__(self, Customer, Bank, Account, Limit, )

    def Charge(self, Price):
        Success = super().Charge(Price)
        if Success:
            self._Balance += 5
            return Success

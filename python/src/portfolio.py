from .missing_exchange_rate_error import MissingExchangeRateError
from .currency import Currency
from .bank import Bank


class Portfolio:
    def __init__(self):
        self.value = 0
        self.currency = Currency.EUR

    def evaluate(self, currency: Currency, bank: Bank):
        try:
            newValue = bank.convert(self.value, self.currency, currency)
        except MissingExchangeRateError as e:
            print("ALEXANDRE")
            raise e

        return newValue

    def add(self, amount: int, currency: Currency):
        self.value += amount

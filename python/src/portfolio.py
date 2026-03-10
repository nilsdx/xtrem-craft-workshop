from .missing_exchange_rate_error import MissingExchangeRateError
from .currency import Currency
from .bank import Bank


class Portfolio:
    def __init__(self):
        self.values = {}
        self.value = 0
        self.currency = Currency.EUR

    def evaluate(self, currency: Currency, bank: Bank):
        newValue = 0
        try:
            for key_currency in self.values.keys():
                newValue += bank.convert(self.values[key_currency], key_currency, currency)
        except MissingExchangeRateError as e:
            raise e

        return newValue

    def add(self, amount: int, currency: Currency):
        if currency in self.values.keys():
            self.values[currency] += amount
        else:
            self.values[currency] = amount

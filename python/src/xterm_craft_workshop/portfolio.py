from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Portfolio:
    def __init__(self):
        self.values = {}

    def evaluatePortfolio(self, currency: Currency, bank: Bank):
        newValue = 0
        try:
            for key_currency in self.values.keys():
                newValue += bank.convertCurrency(Money(self.values[key_currency]
                                                       , key_currency)
                                                       , currency).value
        except MissingExchangeRateError as e:
            raise e

        return newValue

    def addMoney(self, money: Money):
        if money.currency in self.values.keys():
            self.values[money.currency] += money.value
        else:
            self.values[money.currency] = money.value

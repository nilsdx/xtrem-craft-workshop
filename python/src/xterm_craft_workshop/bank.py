from typing import Dict

from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.exchange_rate import ExchangeRate
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, pivot=None, exchange_rate={}) -> None:
        self._exchange_rate = exchange_rate
        self._devise_pivot = None
        self.devise_pivot = pivot
        self.rates = {}

    @property
    def devise_pivot(self):
        return self._devise_pivot

    @devise_pivot.setter
    def devise_pivot(self, new_devise):
        if self._devise_pivot == None:
            self._devise_pivot = new_devise
        else:
            raise ValueError("Il y a déjà une devise.")

    @staticmethod
    def createNewExchangeRate(
        fromCurrency: Currency, toCurrency: Currency, rate: float
    ) -> "Bank":
        bank = Bank()
        bank.addExchangeRate(fromCurrency, toCurrency, rate)

        return bank

    def addExchangeRate(
        self, fromCurrency: Currency, toCurrency: Currency, rate: float
    ) -> None:
        self._exchange_rate[f"{fromCurrency.value}->{toCurrency.value}"] = rate
        self.rates[toCurrency] = ExchangeRate(toCurrency, rate)

    def convertCurrency(self, money: Money, toCurrency: Currency) -> Money:
        if (money.value < 0):
            raise ValueError("Le montant ne peut pas être infèrieur à 0")
        elif toCurrency == money.currency:
            return money
        elif (money.value == 0):
            return Money(0, money.currency)
        elif toCurrency not in self.rates.keys():
            raise MissingExchangeRateError(money.currency, toCurrency)
        elif toCurrency.value not in [item.value for item in Currency]:
            raise ValueError("Devise inconnue")
        # elif toCurrency == self.devise_pivot:
        #     value = money.value * 1/self.rates[toCurrency].rate
            # return Money(value, toCurrency)


        if not (self.canConvert(money.currency, toCurrency)):
            raise MissingExchangeRateError(money.currency, toCurrency)
        return (
            Money(money.value, money.currency)
            if money.currency == toCurrency
            else Money(
                money.value
                * self._exchange_rate[f"{money.currency.value}->{toCurrency.value}"],
                toCurrency,
            )
        )

    def canConvert(self, fromCurrency: Currency, toCurrency: Currency) -> bool:
        return (
            fromCurrency.value == toCurrency.value
            or f"{fromCurrency.value}->{toCurrency.value}" in self._exchange_rate
        )

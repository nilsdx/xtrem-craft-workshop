from typing import Dict
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate={}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def createNewExchangeRate(
        fromCurrency: Currency, toCurrency: Currency, rate: float
    ) -> "Bank":
        bank = Bank({})
        bank.addExchangeRate(fromCurrency, toCurrency, rate)

        return bank

    def addExchangeRate(
        self, fromCurrency: Currency, toCurrency: Currency, rate: float
    ) -> None:
        self._exchange_rate[f"{fromCurrency.value}->{toCurrency.value}"] = rate

    def convertCurrency(
        self, money: Money, toCurrency: Currency
    ) -> Money:
        if not (self.canConvert(money.currency, toCurrency)):
            raise MissingExchangeRateError(money.currency, toCurrency)
        return (
            Money(money.value, money.currency) 
            if money.currency == toCurrency
            else Money(money.value * self._exchange_rate[f"{money.currency.value}->{toCurrency.value}"], toCurrency)
        )

    def canConvert(self, fromCurrency: Currency, toCurrency: Currency) -> bool:
        return (
            fromCurrency.value == toCurrency.value
            or f"{fromCurrency.value}->{toCurrency.value}" in self._exchange_rate
        )

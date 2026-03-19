from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.exchange_rate import ExchangeRate


class BankBuilder:
    def __init__(self) -> None:
        self.pivot_currency = Currency.EUR
        self.exchange_rates = {}
        self.rates = {}

    @staticmethod
    def a_bank() -> "BankBuilder":
        return BankBuilder()

    def with_pivot_currency(self, currency: Currency) -> "BankBuilder":
        self.pivot_currency = currency
        return self

    def with_exchange_rate(self, currency: Currency, rate: float) -> "BankBuilder":
        self.exchange_rates[f"{self.pivot_currency.value}->{currency.value}"] = rate
        self.exchange_rates[f"{currency.value}->{self.pivot_currency.value}"] = 1 / rate
        self.rates[currency] = ExchangeRate(currency, rate)
        return self

    def build(self) -> Bank:
        bank = Bank(self.pivot_currency)
        
        for exchangeRate in self.rates.values():
            bank.addExchangeRate(self.pivot_currency, exchangeRate.currency, exchangeRate.rate)
        
        return bank

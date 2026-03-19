from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency


class BankBuilder:
    def __init__(self) -> None:
        self.pivot_currency = Currency.EUR
        self.exchange_rates = {}

    @staticmethod
    def a_bank() -> "BankBuilder":
        return BankBuilder()

    def with_pivot_currency(self, currency: Currency) -> "BankBuilder":
        self.pivot_currency = currency
        return self

    def with_exchange_rate(self, currency: Currency, rate: float) -> "BankBuilder":
        self.exchange_rates[f"{self.pivot_currency.value}->{currency.value}"] = rate
        self.exchange_rates[f"{currency.value}->{self.pivot_currency.value}"] = 1 / rate
        return self

    def build(self) -> Bank:
        return Bank(self.pivot_currency, self.exchange_rates)

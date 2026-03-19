import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.portfolio import Portfolio
from xterm_craft_workshop.bank_builder import BankBuilder


class TestPortfolio:
    def test_empty_value_portfolio(self):
        portfolio = Portfolio()
        bank = BankBuilder.a_bank().with_pivot_currency(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()

        eval = portfolio.evaluatePortfolio(Currency.EUR, bank)

        assert eval == 0

    def test_portfolio_contains_10_eur(self):
        portfolio = Portfolio()
        bank = BankBuilder.a_bank().with_pivot_currency(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        
        portfolio.addMoney(Money(10, Currency.EUR))
        eval = portfolio.evaluatePortfolio(Currency.EUR, bank)

        assert eval == 10

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_with_exchange_rate(self):
        portfolio = Portfolio()
        bank = BankBuilder.a_bank().with_pivot_currency(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()

        portfolio.addMoney(Money(10, Currency.EUR))
        eval = portfolio.evaluatePortfolio(Currency.USD, bank)

        assert eval == 12

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_without_exchange_rate(self):
        portfolio = Portfolio()
        bank = BankBuilder.a_bank().with_pivot_currency(Currency.EUR).with_exchange_rate(Currency.KRW, 1.2).build()
        portfolio.addMoney(Money(10, Currency.EUR))

        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluatePortfolio(Currency.USD, bank)

        assert str(error.value) == "EUR->USD"

    def test_portfolio_contains_10_eur_and_5_usd_when_evaluate_in_usd(self):
        portfolio = Portfolio()
        bank = BankBuilder.a_bank().with_pivot_currency(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        
        portfolio.addMoney(Money(10, Currency.EUR))
        portfolio.addMoney(Money(5, Currency.USD))

        eval = portfolio.evaluatePortfolio(Currency.USD, bank)

        assert eval == 17

    def test_add_same_currency_values_euro(self):
        portfolio = Portfolio()
        portfolio.addMoney(Money(10, Currency.EUR))
        portfolio.addMoney(Money(15, Currency.EUR))

        assert portfolio.values[Currency.EUR] == 25
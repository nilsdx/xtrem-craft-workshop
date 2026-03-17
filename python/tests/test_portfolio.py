import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError
from python.src.portfolio import Portfolio
from python.src.money import Money


class TestPortfolio:
    def test_empty_value_portfolio(self):
        portfolio = Portfolio()
        bank = Bank({})

        eval = portfolio.evaluatePortfolio(Currency.EUR, bank)

        assert eval == 0

    def test_portfolio_contains_10_eur(self):
        portfolio = Portfolio()
        bank = Bank({})

        portfolio.addMoney(Money(10, Currency.EUR))
        eval = portfolio.evaluatePortfolio(Currency.EUR, bank)

        assert eval == 10

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_with_exchange_rate(self):
        portfolio = Portfolio()
        bank = Bank({})
        bank.addExchangeRate(Currency.EUR, Currency.USD, 1.2)

        portfolio.addMoney(Money(10, Currency.EUR))
        eval = portfolio.evaluatePortfolio(Currency.USD, bank)

        assert eval == 12

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_without_exchange_rate(self):
        portfolio = Portfolio()
        bank = Bank({})
        portfolio.addMoney(Money(10, Currency.EUR))

        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluatePortfolio(Currency.USD, bank)

        assert str(error.value) == "EUR->USD"

    def test_portfolio_contains_10_eur_and_5_usd_when_evaluate_in_usd(self):
        portfolio = Portfolio()
        bank = Bank.createNewExchangeRate(Currency.EUR, Currency.USD, 1.2)

        portfolio.addMoney(Money(10, Currency.EUR))
        portfolio.addMoney(Money(5, Currency.USD))

        eval = portfolio.evaluatePortfolio(Currency.USD, bank)

        assert eval == 17

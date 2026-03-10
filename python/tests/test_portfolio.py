import pytest

from python.src.currency import Currency
from python.src.portfolio import Portfolio
from python.src.bank import Bank
from python.src.missing_exchange_rate_error import MissingExchangeRateError


class TestPortfolio:
    def test_empty_value_portfolio(self):
        portfolio = Portfolio()
        bank = Bank({})

        eval = portfolio.evaluate(Currency.EUR, bank)

        assert(eval == 0)

    def test_portfolio_contains_10_eur(self):
        portfolio = Portfolio()
        bank = Bank({})

        portfolio.add(10, Currency.EUR)
        eval = portfolio.evaluate(Currency.EUR, bank)

        assert (eval == 10)

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_with_exchange_rate(self):
        portfolio = Portfolio()
        bank = Bank({})
        bank.addExchangeRate(Currency.EUR, Currency.USD, 1.2)

        portfolio.add(10, Currency.EUR)
        eval = portfolio.evaluate(Currency.USD, bank)

        assert(eval == 12)

    def test_portfolio_contains_10_eur_when_evaluate_in_usd_without_exchange_rate(self):
        portfolio = Portfolio()
        bank = Bank({})
        portfolio.add(10, Currency.EUR)

        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(Currency.USD, bank)

        assert str(error.value) == "EUR->USD"

    def test_portfolio_contains_10_eur_and_5_usd_when_evaluate_in_usd(self):
        portfolio = Portfolio()
        bank = Bank.createNewExchangeRate(Currency.EUR, Currency.USD, 1.2)
        
        portfolio.add(10, Currency.EUR)
        portfolio.add(5, Currency.USD)

        eval = portfolio.evaluate(Currency.USD, bank)

        assert(eval == 17)
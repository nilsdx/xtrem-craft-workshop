import pytest

from tests.bank_builder import BankBuilder
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money


class TestBank:
    def test_convert_euro_to_usd_returns_float(self):
        # arrange
        bank = (
            BankBuilder.a_bank()
            .with_pivot_currency(Currency.EUR)
            .with_exchange_rate(Currency.USD, 1.2)
            .build()
        )
        money = Money(10, Currency.EUR)
        # act
        result = bank.convertCurrency(money, Currency.USD)
        # assert
        assert result.value == 12

    def test_convert_euro_to_usd_returns_same_value(self):
        # arrange
        bank = (
            BankBuilder.a_bank()
            .with_pivot_currency(Currency.EUR)
            .with_exchange_rate(Currency.USD, 1)
            .build()
        )
        money = Money(10, Currency.EUR)
        # act
        result = bank.convertCurrency(money, Currency.EUR)
        # assert
        assert result.value == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self):
        # arrange
        bank = (
            BankBuilder.a_bank()
            .with_pivot_currency(Currency.EUR)
            .with_exchange_rate(Currency.USD, 1.2)
            .build()
        )
        money = Money(10, Currency.EUR)
        # act
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convertCurrency(money, Currency.KRW)
        # assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self):
        # arrange
        bank = (
            BankBuilder.a_bank()
            .with_pivot_currency(Currency.EUR)
            .with_exchange_rate(Currency.USD, 1.2)
            .build()
        )
        money = Money(10, Currency.EUR)
        # act
        result = bank.convertCurrency(money, Currency.USD)
        # assert
        assert result.value == 12

        # act
        bank.addExchangeRate(Currency.EUR, Currency.USD, 1.3)
        # assert
        assert bank.convertCurrency(money, Currency.USD).value == 13

    # def test_no_pivot(self):
    #     with pytest.raises(ValueError) as error:
    #         bank = (
    #             BankBuilder.a_bank()
    #             .build()
    #         )
    #     assert error.value == "Missing pivot"
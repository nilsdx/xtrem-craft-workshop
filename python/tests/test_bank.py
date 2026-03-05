import pytest
import re

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError


class TestBank:
    def test_convert_euro_to_usd_returns_float(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        # act
        result = bank.convert(10, Currency.EUR, Currency.USD)
        # assert
        assert result == 12

    def test_convert_euro_to_usd_returns_same_value(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        # act
        result = bank.convert(10, Currency.EUR, Currency.EUR)
        # assert
        assert result == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        # act
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(10, Currency.EUR, Currency.KRW)
        # assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self):
        # arrange
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        # act
        result = bank.convert(10, Currency.EUR, Currency.USD)
        # assert
        assert result == 12

        # act
        bank.addEchangeRate(Currency.EUR, Currency.USD, 1.3)
        # assert
        assert bank.convert(10, Currency.EUR, Currency.USD) == 13

    

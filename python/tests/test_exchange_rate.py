import pytest

from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.exchange_rate import ExchangeRate
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class TestExchangeRate:
    def test_adding_negative_exchange_rate_throws_exception(self):
        # arrange + act
        with pytest.raises(ValueError) as error:
            rate = ExchangeRate(Currency.EUR, -2.3)
        # assert
        assert str(error.value) == "Rate cannot be negative"
    def test_cannot_create_null_exchange_rate(self):
                # arrange + act
        with pytest.raises(ValueError) as error:
            rate = ExchangeRate(Currency.EUR, 0)
        # assert
        assert str(error.value) == "Rate cannot be null"

    def test_cannot_create_empty_exchange_rate(self):
                # arrange + act
        with pytest.raises(ValueError) as error:
            rate = ExchangeRate(Currency.EUR, None) # type: ignore
        # assert
        assert str(error.value) == "Rate cannot be empty"
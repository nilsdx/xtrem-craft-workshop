from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.money_calculator import MoneyCalculator


class TestMoney:
    def test_add_in_usd_returns_value(self):
        assert isinstance(MoneyCalculator.add(5, 10), float)
        assert MoneyCalculator.add(5, 10) is not None

    def test_multiply_in_euros_returns_positive_number(self):
        assert MoneyCalculator.times(10, 2) > 0

    def test_divide_in_korean_won_returns_float(self):
        assert MoneyCalculator.divide(4002, 4) == 1000.5

    def test_add_euro_to_euro_returns_euro(self):
        money1 = Money(value=5, currency=Currency.EUR)
        money2 = Money(value=10, currency=Currency.EUR)

        res = money1 + money2

        assert res == Money(15, Currency.EUR)

    def test_multiply_euro_to_int_returns_euro(self):
        money = Money(value=5, currency=Currency.EUR)

        res = 3 * money

        assert res == Money(15, Currency.EUR)

        res = money * 3

        assert res == Money(15, Currency.EUR)

    def test_substract_euro_to_euro_returns_euro(self):
        money1 = Money(value=5, currency=Currency.EUR)
        money2 = Money(value=10, currency=Currency.EUR)

        res = money2 - money1

        assert res == Money(5, Currency.EUR)

    def test_divide_euro_to_int_returns_euro(self):
        money = Money(value=10, currency=Currency.EUR)
        res = money / 2

        assert res == Money(value=5, currency=Currency.EUR)

from dataclasses import dataclass
from typing import Self

from .currency import Currency


@dataclass(frozen=True, init=True, eq=True)
class Money:
    value: float
    currency: Currency

    def __add__(self, other: Self):
        return Money(self.value + other.value, self.currency)

    def __mul__(self, other: int):
        return Money(self.value * other, self.currency)

    def __rmul__(self, other: int):
        return Money(self.value * other, self.currency)

    def __sub__(self, other : Self):
        return Money(self.value - other.value,self.currency)

    def __truediv__(self, other : int):
        return Money(self.value / other, self.currency)

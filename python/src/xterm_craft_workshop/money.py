from dataclasses import dataclass
from typing import Self

from .currency import Currency


@dataclass(frozen=True, init=True, eq=True)
class Money:
    value: float
    currency: Currency

    def __post_init__(self):
        if self.currency is None:
            raise ValueError("La devise (currency) ne peut pas être None.")
        
        if self.value is None:
            raise ValueError("La valeur (value) ne peut pas être None.")

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

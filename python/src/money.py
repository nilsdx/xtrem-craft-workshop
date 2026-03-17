from dataclasses import dataclass
from typing import Self
from .currency import Currency

@dataclass(frozen=True, init=True, eq=True)
class Money:
    value: int
    currency: Currency

    def __add__(self, other: Self):
        return Money(self.value + other.value, self.currency)
    
    def __rmul__(self, other: int):
        return Money(self.value * other, self.currency)
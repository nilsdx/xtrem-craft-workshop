from dataclasses import dataclass
from .currency import Currency

@dataclass(frozen=True, init=True, eq=True)
class Money:
    value: int
    currency: Currency

    def __add__(self, other):
        return Money(self.value + other.value, self.currency)
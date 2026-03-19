from dataclasses import dataclass
from typing import Self

from .currency import Currency


@dataclass(frozen=True, init=True, eq=True)
class ExchangeRate:
    currency: Currency
    rate: float

    def __post_init__(self):
        if self.rate == None:
            raise ValueError("Rate cannot be empty")
        if self.rate < 0:
            raise ValueError("Rate cannot be negative")
        if self.rate == 0:
            raise ValueError("Rate cannot be null")
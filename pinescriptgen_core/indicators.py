from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)


# Se utiliza el IndicatorFactory para generar el indicador correcto desde Pinescriptgenerator.py
class IndicatorFactory:
    @staticmethod
    def create_indicator(indicator_name: str, value: Optional[int] = None):
        if indicator_name == "ema":
            return EMAIndicator(value)
        elif indicator_name == "sma":
            return SMAIndicator(value)
        elif indicator_name == "price":
            return CloseIndicator()
        elif indicator_name == "adx":
            return AdxIndicator(value)
        elif indicator_name == "cci":
            return CciIndicator(value)
        elif indicator_name == "dmi+":
            return DmiPlusIndicator(value)
        elif indicator_name == "dmi-":
            return DmiMinusIndicator(value)
        elif indicator_name == "macd":
            return MacdIndicator(value)
        elif indicator_name == "rsi":
            return RSIIndicator(value)
        elif indicator_name == "lineaDe":
            return LineaSenyalIndicator(value)
        elif indicator_name == "nivel":
            return NivelIndicator(value)
        else:
            raise ValueError(f"Invalid indicator type: {indicator_name}")


# TODO: Delete old abstract indicator base class
@dataclass
class OldAbstractIndicator(ABC):
    """Abstract Indicator"""

    @abstractmethod
    def formatted(self):
        pass


@dataclass
class AbstractIndicator(ABC):
    """Abstract Indicator"""
    value: Optional[int] = None

    def __post_init__(self):
        if self.value is not None:
            self.value = int(self.value)  # Convert to int

    @abstractmethod
    def formatted(self):
        pass


# TODO: Delete Indiactor class
@dataclass
class Indicator(OldAbstractIndicator):
    """Concrete Indicator"""
    type: str
    value: Optional[float] = None


@dataclass
class EMAIndicator(AbstractIndicator):
    def formatted(self):
        return f"ta.ema(close, {self.value})"


@dataclass
class SMAIndicator(AbstractIndicator):
    """SMA Indicator"""

    def formatted(self):
        return f"ta.sma(close, {self.value})"


@dataclass
class RSIIndicator(AbstractIndicator):
    def formatted(self):
        return f"ta.rsi(close, {self.value})"


@dataclass
class CloseIndicator(AbstractIndicator):
    def formatted(self):
        return f"close"


@dataclass
class AdxIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"


@dataclass
class CciIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"


@dataclass
class DmiPlusIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"


@dataclass
class DmiMinusIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"

@dataclass
class MacdIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"


@dataclass
class LineaSenyalIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"

@dataclass
class NivelIndicator(AbstractIndicator):
    def formatted(self):
        return f"implementation_pending"
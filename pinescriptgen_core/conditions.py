from abc import ABC
from dataclasses import dataclass
from typing import Optional
import logging
from pinescriptgen_core.indicators import AbstractIndicator

logger = logging.getLogger(__name__)


@dataclass
class AbstractCondition:
    """ Abstract Base Class para Condition"""


@dataclass
class Condition(AbstractCondition):
    """Concrete Condition"""
    condition: Optional[str]
    indicatorA: Optional[AbstractIndicator] = None
    indicatorB: Optional[AbstractIndicator] = None

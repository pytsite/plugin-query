"""PytSite Query Plugin Comparison Operators
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any as _Any
from ._operator import FieldOperator as _FieldOperator


class ComparisonOperator(_FieldOperator):
    def __init__(self, field: str, arg: _Any):
        """Init
        """
        super().__init__(field)

        self._arg = arg

    @property
    def arg(self) -> _Any:
        return self._arg

    @arg.setter
    def arg(self, value: _Any):
        self._arg = value

    def compile(self) -> dict:
        """Get representation of operator's content
        """
        return {self._field: {self.name: self._arg}}


class Eq(ComparisonOperator):
    pass


class Gt(ComparisonOperator):
    pass


class Gte(ComparisonOperator):
    pass


class In(ComparisonOperator):
    pass


class Lt(ComparisonOperator):
    pass


class Lte(ComparisonOperator):
    pass


class Ne(ComparisonOperator):
    pass


class Nin(ComparisonOperator):
    pass

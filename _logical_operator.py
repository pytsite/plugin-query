"""PytSite Query Plugin Logical Operators
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union, Iterator as _Iterator
from ._operator import Operator as _Operator


class LogicalOperator(_Operator):
    def __init__(self, operators: _Union[_Operator, _Iterator[_Operator]] = None):
        """Init
        """
        self._operators = []    # type: [_Operator]

        if operators:
            for op in operators if hasattr(operators, '__iter__') else [operators]:
                self.add(op)

    def add(self, op: _Operator):
        if not isinstance(op, _Operator):
            raise TypeError('{} expected, got {}'.format(_Operator, type(op)))

        self._operators.append(op)

    def compile(self) -> dict:
        """Get data representation of operator's content
        """
        return {self.name: [op.compile() for op in self]}

    def __len__(self):
        return len(self._operators)

    def __iter__(self):
        return iter(self._operators)

    def __getitem__(self, key):
        return self._operators[key]

    def __delitem__(self, key):
        del self._operators[key]

    def __contains__(self, item):
        return item in self._operators


class And(LogicalOperator):
    pass


class Not(LogicalOperator):
    pass


class Nor(LogicalOperator):
    pass


class Or(LogicalOperator):
    pass

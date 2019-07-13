"""PytSite Query Plugin Logical Operators
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union, Iterator
from ._operator import Operator


class LogicalOperator(Operator):
    def __init__(self, operators: Union[Operator, Iterator[Operator]]):
        """Init
        """
        self._operators = []  # type: [Operator]
        for op in operators if hasattr(operators, '__iter__') else [operators]:
            self.add(op)

    def add(self, op: Operator):
        if not isinstance(op, Operator):
            raise TypeError('{} expected, got {}'.format(Operator, type(op)))

        self._operators.append(op)

    def compile(self) -> dict:
        """Get data representation of operator's content
        """
        r = {self.name: [op.compile() for op in self if op]}

        return r if r[self.name] else {}

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

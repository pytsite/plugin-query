"""PytSite Query Plugin Query Class
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union, List as _List, Iterator as _Iterator
from pytsite import util as _util
from ._operator import Operator as _Operator


class Query:
    def __init__(self, operators: _Union[_Operator, _Iterator[_Operator]] = None):
        self._operators = []  # type: _List[_Operator]

        if operators:
            for op in operators if hasattr(operators, '__iter__') else [operators]:
                self.add(op)

    @property
    def operators(self) -> _List[_Operator]:
        return self._operators

    @operators.setter
    def operators(self, value: _List[_Operator]):
        self._operators = value

    def add(self, op: _Operator):
        """Add a query clause
        """
        self._operators.append(op)

        return op

    def compile(self) -> dict:
        """Compile the query
        """
        r = {}

        for op in self:
            r = _util.dict_merge(r, op.compile())

        return r

    def __eq__(self, other) -> bool:
        return self.compile() == other.compile()

    def __len__(self) -> int:
        return len(self._operators)

    def __iter__(self) -> _Iterator[_Operator]:
        return iter(self._operators)

    def __str__(self) -> str:
        return str(self.compile())

    def __getitem__(self, key):
        return self._operators[key]

    def __delitem__(self, key):
        del self._operators[key]

    def __contains__(self, item):
        return item in self._operators

"""PytSite Query Plugin Query Class
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union, List as _List, Iterator as _Iterator
from pytsite import util as _util
from ._operator import Operator as _Operator
from ._logical_operator import LogicalOperator as _LogicalOperator, And as _And


class Query:
    def __init__(self, operators: _Union[_Operator, _Iterator[_Operator]] = None, query = None):
        self._operators = []  # type: _List[_Operator]

        if operators:
            if not isinstance(operators, (list, tuple)):
                operators = [operators]

            for op in operators:
                self.add(op)

        if isinstance(query, Query):
            for op in query:
                self.add(op)

    def add(self, op: _Operator):
        """Add a query clause
        """
        if not isinstance(op, _Operator):
            raise TypeError('{} expected, got {}'.format(_Operator, type(op)))

        if not isinstance(op, _LogicalOperator):
            op = _And(op)

        self._operators.append(op)

        return op

    def compile(self) -> dict:
        """Compile the query
        """
        r = {}

        for op in self:
            r = _util.dict_merge(r, op.compile())

        return r

    def __len__(self) -> int:
        return len(self._operators)

    def __iter__(self) -> _Iterator[_Operator]:
        return iter(self._operators)

    def __str__(self) -> str:
        return str(self.compile())

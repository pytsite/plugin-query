"""PytSite Query Plugin Query Class
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union, List, Iterator
from dicmer import dict_merge
from ._operator import Operator, FieldOperator
from ._logical_operator import LogicalOperator


class Query:
    def __init__(self, operators: Union[Operator, Iterator[Operator]] = None):
        """Init
        """
        self._operators = []  # type: List[Operator]

        if operators:
            for op in operators if hasattr(operators, '__iter__') else [operators]:
                self.add(op)

    @property
    def operators(self) -> List[Operator]:
        """Get operators
        """
        return self._operators

    @operators.setter
    def operators(self, value: List[Operator]):
        """Set operators
        """
        self._operators = value

    def add(self, op: Operator):
        """Add an operator
        """
        self._operators.append(op)

        return op

    def rm_field(self, field: str, _root: Operator = None):
        """Remove all FieldOperators of particular field
        """
        if _root is None:
            _root = self

        ops_to_del = []
        for i, op in enumerate(_root):
            if isinstance(op, LogicalOperator):
                self.rm_field(field, op)
            elif isinstance(op, FieldOperator) and op.field == field:
                ops_to_del.append(i)

        for i in ops_to_del:
            del _root[i]

        return self

    def compile(self) -> dict:
        """Compile the query
        """
        r = {}

        for op in self:
            r = dict_merge(r, op.compile())

        return r

    def __eq__(self, other) -> bool:
        return self.compile() == other.compile()

    def __len__(self) -> int:
        return len(self.compile())

    def __iter__(self) -> Iterator[Operator]:
        return iter(self._operators)

    def __str__(self) -> str:
        return str(self.compile())

    def __getitem__(self, key):
        return self._operators[key]

    def __delitem__(self, key):
        del self._operators[key]

    def __contains__(self, item):
        return item in self._operators

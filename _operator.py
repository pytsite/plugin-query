"""PytSite Query Plugin Base Operator
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Operator:
    @property
    def name(self) -> str:
        return '$' + self.__class__.__name__[:1].lower() + self.__class__.__name__[1:]

    def compile(self) -> dict:
        """Get representation of operator's content
        """
        raise NotImplementedError()


class FieldOperator(Operator):
    def __init__(self, field: str):
        self._field = field

    @property
    def field(self) -> str:
        return self._field

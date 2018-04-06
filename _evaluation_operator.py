"""PytSite Query Plugin Evaluation Operators
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from ._operator import Operator as _Operator, FieldOperator as _FieldOperator


class EvaluationOperator(_Operator):
    pass


class Text(EvaluationOperator):
    def __init__(self, search: str, language: str, case_sensitive: bool = False, diacritic_sensitive: bool = False):
        """Init
        """
        self._search = search
        self._language = language
        self._case_sensitive = case_sensitive
        self._diacritic_sensitive = diacritic_sensitive

    def compile(self) -> dict:
        """Get representation of operator's content
        """
        return {
            '$text': {
                '$search': self._search,
                '$language': self._language,
                '$caseSensitive': self._case_sensitive,
                '$diacriticSensitive': self._diacritic_sensitive,
            }
        }


class Regex(EvaluationOperator, _FieldOperator):
    def __init__(self, field: str, pattern: str, case_insensitive: bool = False, multiline: bool = False,
                 dot_all: bool = False, verbose: bool = False):
        """Init
        """
        super().__init__(field)

        self._field = field

        self._pattern = pattern
        self._options = ''

        if case_insensitive:
            self._options += 'i'
        if multiline:
            self._options += 'm'
        if dot_all:
            self._options += 's'
        if verbose:
            self._options += 'x'

    def compile(self) -> dict:
        """Get representation of operator's content
        """
        return {
            self._field: {
                '$regex': self._pattern,
                '$options': self._options,
            }
        }

"""PytSite Query Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._query import Query
from ._operator import Operator, FieldOperator
from ._logical_operator import LogicalOperator, And, Nor, Not, Or
from ._comparison_operator import ComparisonOperator, Eq, Gt, Gte, In, Lt, Lte, Ne, Nin
from ._evaluation_operator import EvaluationOperator, Text, Regex
from ._geospatial_operator import GeospatialOperator, Near, NearSphere

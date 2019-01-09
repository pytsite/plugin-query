# PytSite Query Plugin


## Changelog


### 1.2 (2018-01-09)

- `LogicalOperator.operators` constructor made required.
- `LogicalOperator.compile()`'s return value cleanup added.
- Incorrect `Query.__len__()`'s return value fixed.


### 1.1 (2018-01-07)

- New `Query.operators` getter and setter.
- New methods in `Query`: `__eq__()`, `__getitem__()`, `__delitem__()`,
  `__contains__`.
- New methods in `Operator`: `__str__()`, `__eq__()`.
- New methods in `LogicalOperator`: `add()`, `__getitem()__`,
  `__delitem__()`, `__contains__()`.
- Unnecessary `query` arg removed from `Query.__init__()`.


### 1.0.2 (2018-10-05)

Cleanup.


### 1.0.1 (2018-04-13)

Text search operator language checking added.


### 1.0 (2018-04-06)

First release.

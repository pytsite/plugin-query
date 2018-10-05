"""PytSite Query Plugin Geospatial Operators
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from ._operator import FieldOperator as _FieldOperator


class GeospatialOperator(_FieldOperator):
    pass


class Near(GeospatialOperator):
    def __init__(self, field: str, lng: float, lat: float, max_distance: int = None, min_distance: int = None):
        """Init
        """
        super().__init__(field)

        self._lng = lng
        self._lat = lat
        self._max_distance = max_distance
        self._min_distance = min_distance

    def compile(self) -> dict:
        """Get representation of operator's content
        """
        r = {
            self._field: {
                self.name: {
                    '$geometry': {
                        'type': 'Point',
                        'coordinates': [self._lat, self._lng],
                    }
                }
            }
        }

        if self._max_distance is not None:
            r[self._field]['$near']['$maxDistance'] = self._max_distance

        if self._min_distance is not None:
            r[self._field]['$near']['$minDistance'] = self._min_distance

        return r


class NearSphere(Near):
    pass

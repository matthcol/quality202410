# convention de nommage: communauté + des équipes de developpment
# Python: PEP 8
# https://peps.python.org/pep-0008/

from dataclasses import dataclass

from computing.model.point import Point


@dataclass
class Circle:
    center: Point
    radius: float

    def surface(self) -> float:
        raise NotImplementedError
    
    def perimeter(self) -> float:
        raise NotImplementedError

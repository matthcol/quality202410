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
    
    def translate(self, delta_x, delta_y) -> None:
        """ translate this circle with relative horizontal and vertical offsets

        Arguments:
        ----------
        - delta_x (float): horizontal offset
        - delta_y (float): vertical offset
        """
        raise NotImplementedError

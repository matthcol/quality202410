from dataclasses import dataclass

from computing.model.point import Point


@dataclass
class Polygon:
    vertices: list[Point]

    def perimeter(self) -> float:
        return 0.0
    
    def surface(self) -> float:
        return 0.0
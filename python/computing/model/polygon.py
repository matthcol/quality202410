from dataclasses import dataclass

from computing.model.point import Point


@dataclass
class Polygon:
    vertices: list[Point]

    def perimeter(self) -> float:
        prev = self.vertices[-1]
        p = 0.0
        for v in self.vertices:
            p += prev.distance(v)
            prev = v
        return p
    
    def surface(self) -> float:
        return 0.0
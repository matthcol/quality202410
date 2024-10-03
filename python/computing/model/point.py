from dataclasses import dataclass

# NB: rédaction simplifiée de classe
# - @dataclass: inlus dans python >= 3.8
# - pydantic (lib tierce): +value validation
@dataclass
class Point:
    x: float
    y: float
    name: str | None = None

    def distance(self, other: 'Point') -> float:
        raise NotImplementedError()
    
    def translate(self, delta_x, delta_y):
        raise NotImplementedError()
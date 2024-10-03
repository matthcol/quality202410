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
    
    def translate(self, delta_x: float, delta_y: float) -> None:
        """ translate this point with relative horizontal and vertical offsets

        Arguments:
        ----------
        - delta_x (float): horizontal offset
        - delta_y (float): vertical offset
        """
        self.x += delta_x
        self.y += delta_y
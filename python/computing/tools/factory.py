import math
from computing.model.circle import Circle
from computing.model.point import Point


def new_valid_circle(center: Point, radius: float) -> Circle:
    """create a valid new circle with its center and radius.
    Check if radius is valid: >0 and not NaN.
    NB: radius can be +inf
    
    Arguments:
    - center (Point): center of the new circle
    - radius (float): radius of the ne circle

    Exception:
    - ValueError("invalid circle") if radius is <= 0 or NaN
    """
    if radius <=0 or math.isnan(radius):
        raise ValueError("invalid circle")
    return Circle(center=center, radius=radius)


# wrong code checked by a type checker (mypy)
# if __name__ == '__main__':
#     c = new_valid_circle(12, "grand")
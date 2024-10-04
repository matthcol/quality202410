import math
import pytest

from computing.tools.factory import new_valid_circle

@pytest.mark.parametrize(
        "radius",
        [5E-324, 0.1, 1.0, 56.625, 1E308, math.inf]
)
def test_new_valid_circle_ok(radius, point_average):
    c = new_valid_circle(point_average, radius=radius)
    assert radius == c.radius
    assert c.center is point_average

@pytest.mark.parametrize(
        "bad_radius",
        [0.0, -5E-324, -0.1, -1.0, -56.625, -1E308, -math.inf, math.nan, float('inf') / float('inf')]
)
def test_new_valid_circle_error(bad_radius, point_average):
    with pytest.raises(ValueError) as exc:
        new_valid_circle(center=point_average, radius=bad_radius)
    assert "invalid circle" == str(exc.value)

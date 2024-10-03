import math
import pytest
from computing.geometry import distance

@pytest.fixture
def triangle_345() -> tuple[float, float, float]:
    return (3.0, 4.0, 5.0)

def test_hypot_345(triangle_345):
    a, b, c = triangle_345
    assert math.hypot(a, b) == c

@pytest.mark.parametrize(
        # ["x1", "y1", "x2", "y2", "expected_distance", "relative_margin"],
        "x1, y1, x2, y2, expected_distance, relative_margin",
        [
            (3.5, 4.25, 7.5, 1.25, 5.0, 0.0),
            (3.5E307, 4.25E307, 7.5E307, 1.25E307, 5E307, 0.0),
            (3.5E-314, 4.25E-314, 7.5E-314, 1.25E-314, 5E-314, 1E-6),
        ],
        ids = [
            "median",
            "big_limit",
            "small_limit"
        ]
)
def test_distance(
        x1: float, y1: float, 
        x2: float, y2: float, 
        expected_distance: float, 
        relative_margin: float
):
    actual_distance = distance((x1, y1), (x2, y2))
    assert pytest.approx(actual_distance, rel=relative_margin) == expected_distance
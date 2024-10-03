import pytest
from computing.model.circle import Circle

REL_PRECISION = 1E-15

@pytest.fixture
def circle_average(point_average):
    return Circle(center=point_average, radius=4.5)

def test_perimeter(circle_average):
    assert pytest.approx(circle_average.perimeter(), REL_PRECISION) == 28.274333882308138, "perimeter"

def test_surface(circle_average):
    assert pytest.approx(circle_average.surface(), REL_PRECISION) == 63.61725123519331, "surface"

def test_translate(circle_average):
    circle_average.translate(-1.25, 2.5)
    assert circle_average.center.x == 3.5, "center abscissa X has changed"
    assert circle_average.center.y == 14.75, "center ordinate Y has changed"
    assert circle_average.radius == 4.5, "radius unchanged"
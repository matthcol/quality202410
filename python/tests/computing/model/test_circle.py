import pytest
from pytest_mock import mocker
from computing.model.circle import Circle

REL_PRECISION = 1E-15

@pytest.fixture
def circle_average(point_average):
    return Circle(center=point_average, radius=4.5)

def test_perimeter(circle_average):
    assert pytest.approx(circle_average.perimeter(), REL_PRECISION) == 28.274333882308138, "perimeter"

def test_surface(circle_average):
    assert pytest.approx(circle_average.surface(), REL_PRECISION) == 63.61725123519331, "surface"

def test_translate(circle_average, mocker):
    # Arange: ficture circle average 
    # + mock method translate of the center of thecircle
    mock_translate = mocker.patch.object(circle_average.center, 'translate')
    # Act:
    circle_average.translate(-1.25, 2.5)
    # Assert:
    mock_translate.assert_called_once_with(delta_x=-1.25, delta_y=2.5)

    # NB: Following assertions have been verified in the unit test of Point.translate
    #   and can be check in an integration test
    # assert circle_average.center.x == 3.5, "center abscissa X has changed"
    # assert circle_average.center.y == 14.75, "center ordinate Y has changed"
    # assert circle_average.radius == 4.5, "radius unchanged"
import pytest
from computing.model.point import Point

# fixtures
# https://docs.pytest.org/en/stable/reference/fixtures.html
# https://docs.pytest.org/en/stable/how-to/fixtures.html
# https://docs.pytest.org/en/stable/explanation/fixtures.htm


@pytest.fixture
def point_anonymous():
    return Point(x=3.5, y=12.25)

# tests

def test_distance(point_a, point_b, mocker):
    mock_distance = mocker.patch('computing.geometry.distance', return_value=5.0)
    # Act:
    d = point_a.distance(point_b)
    # Assert: 1 - return value 
    assert d == 5.0
    # Assert: 2 - mock has been called
    mock_distance.assert_called_once_with((point_a.x, point_a.y),(point_b.x, point_b.y))
    

def test_translate_with_local_variable():
    # Arange: 1 object Point
    p = Point(x=3.5, y=12.25)
    # Act: invoke method translate
    p.translate(-1.25, 2.5)
    ## Assert
    assert p.x == 2.25, "abscissa x has been modifed"
    assert p.y == 14.75, "ordinate y has been modified"

def test_translate_with_local_fixture(point_anonymous):
    # Arange: arg point_anonymous provided by fixture with same name
    # Act: invoke method translate
    point_anonymous.translate(-1.25, 2.5)
    ## Assert
    assert point_anonymous.x == 2.25, "abscissa x has been modifed"
    assert point_anonymous.y == 14.75, "ordinate y has been modified"

def test_translate_with_shared_fixture(point_average):
    # Arange: arg point_anonymous provided by fixture with same name
    # Act: invoke method translate
    point_average.translate(1.25, -2.5)
    ## Assert
    assert point_average.x == 6.0, "abscissa x has been modifed"
    assert point_average.y == 9.75, "ordinate y has been modified"
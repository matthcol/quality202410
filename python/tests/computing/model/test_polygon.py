import pytest

from computing.model.polygon import Polygon

@pytest.fixture
def triangle_abc(point_a, point_b, point_c):
    return Polygon(vertices=[
        point_a,
        point_b,
        point_c
    ])

def test_perimeter_triangle(triangle_abc, mocker):
    # Arange
    dist_mock_a = mocker.patch.object(triangle_abc.vertices[0], 'distance', return_value=5)
    dist_mock_b = mocker.patch.object(triangle_abc.vertices[1], 'distance', return_value=4)
    dist_mock_c = mocker.patch.object(triangle_abc.vertices[2], 'distance', return_value=3)
    # Act
    p = triangle_abc.perimeter()
    # Assert: return value
    assert p == 12
    # Assert: mocks have been called once
    assert dist_mock_a.call_count == 1
    assert dist_mock_b.call_count == 1
    assert dist_mock_c.call_count == 1
    # Assert: mocks have been called once with right arg !!! Bug
    # assert dist_mock_a.assert_called_once_with(triangle_abc.vertices[1])
    # assert dist_mock_b.assert_called_once_with(triangle_abc.vertices[2])
    # assert dist_mock_c.assert_called_once_with(triangle_abc.vertices[0])

def test_perimeter_quadrilatere(mocker):
    pass

def test_surface():
    pass
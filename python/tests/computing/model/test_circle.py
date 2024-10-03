import pytest

from computing.model.circle import Circle



@pytest.fixture
def circle_average(point_average):
    return Circle(center=point_average, radius=4.5)
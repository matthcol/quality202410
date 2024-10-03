import pytest
from computing.model.point import Point

@pytest.fixture
def point_average():
    return Point(x=4.75, y=12.25, name="P")
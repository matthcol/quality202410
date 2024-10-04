import pytest
from computing.model.point import Point

@pytest.fixture
def point_a():
    return Point(x=3.5, y=20.5, name="A")

@pytest.fixture
def point_b():
    return Point(x=6.5, y=24.5, name="B")

@pytest.fixture
def point_c():
    return Point(x=6.5, y=20.5, name="C")
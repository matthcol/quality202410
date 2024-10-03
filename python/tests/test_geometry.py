# file regrouping all unit tests of module geometry
import pytest
from geometry import distance


def test_distance_median():
    assert distance((3.5, 4.25), (7.5, 1.25)) == 5.0

def test_distance_median2():
    assert distance((3.1, 4.2), (7.1, 1.2)) == 5.0

def test_distance_big():
    assert distance((350.0, 425.0), (750.0, 125.0)) == 500.0

def test_distance_small():
    assert distance((350.0, 425.0), (750.0, 125.0)) == 500.0

def test_distance_bigger():
    assert distance((3.5E153,4.25E153), (7.5E153, 1.25E153)) == 5E153
    
def test_distance_smaller():
    assert distance((3.5E-153,4.25E-153), (7.5E-153, 1.25E-153)) == 5E-153

def test_distance_bigger_limit():
    assert distance((3.5E307, 4.25E307), (7.5E307, 1.25E307)) == 5E307
    
def test_distance_smaller_limit():
    actual_distance = distance((3.5E-314,4.25E-314), (7.5E-314, 1.25E-314))
    assert pytest.approx(actual_distance, rel=1E-6) == 5E-314
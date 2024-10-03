import numpy as np

# NB: x can have any type which accept "+" operator with int
def inc(x):
    return x + 1

def test_inc_int():
    assert inc(2) == 3

def test_inc_float():
    assert inc(3.5) == 4.5

def test_inc_ndarray():
    x = np.array([1.5, 2.25, 3.75])
    expected_result = np.array([2.5, 3.25, 4.75])
    assert (inc(x) == expected_result).all()

def test_fail():
    "demo failing test, it's not a true unit test"
    assert False
    
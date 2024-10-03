

import pytest

from computing.fibonacci import fibo_binet, fibo_iterative


@pytest.mark.parametrize(
    "n, expected_result",
    [
        # single cases
        (0, 0),
        (1, 1),
        # with formula
        (2, 1),
        (10, 55),
        (51, 20_365_011_074),
    ]
)
def test_fibo_binet(n, expected_result):
    assert fibo_binet(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result",
    [
        # single cases
        (0, 0),
        (1, 1),
        # with formula
        (2, 1),
        (10, 55),
        (51, 20_365_011_074),
    ]
)
def test_fibo_iterative(n, expected_result):
    assert fibo_iterative(n) == expected_result
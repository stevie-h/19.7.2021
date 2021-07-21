# ex23

import pytest
import math_utils


@pytest.mark.parametrize("x, y, expected", [(6, 7, 7), (-8, 2, 2)])
def test_compare(x, y, expected):
    assert math_utils.compare(x, y) == expected


def test_compare_exception():
    with pytest.raises(Exception):
        math_utils.compare(1, 1)


@pytest.mark.parametrize("n, expected", [(3, True), (5, False)])
def test_three_multiple(n, expected):
    assert math_utils.three_multiple(n) == expected


@pytest.mark.parametrize("a, n, expected", [(2, 3, 8), (1, 3, 1), (0, 1, 0)])
def test_power(a, n, expected):
    assert math_utils.power(a, n) == expected


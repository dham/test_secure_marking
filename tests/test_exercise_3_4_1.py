try:
    from polynomials import Polynomial
except ImportError:
    pass
import pytest


@pytest.mark.parametrize(
    "a, b, difference",
    (((0,), (0, 1), (0, -1)),
     ((2, 0, 3), (1, 2), (1, -2, 3)),
     ((4, 2), (10, 2, 4), (-6, 0, -4)))
    )
def test_sub(a, b, difference):
    pass


def test_sub_scalar():
    pass


def test_reverse_sub_scalar():
    pass

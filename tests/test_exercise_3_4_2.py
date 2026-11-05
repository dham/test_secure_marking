try:
    from polynomials import Polynomial
except ImportError:
    pass
import pytest


@pytest.mark.parametrize(
    "f, g, fg", (
     ((1, 1, 1), (1, 1, 1, 1), (1, 2, 3, 3, 2, 1)),
     ((1, 1, 1, 1), (1, 1, 1), (1, 2, 3, 3, 2, 1)),
     ((5, 0, 10, 6), (1, 2, 4), (5, 10, 30, 26, 52, 24)),
     ((0, -2, 9), (1, -4, 1.4, -9), (0, -2, 17, -38.8, 30.6, -81)),
     ((1, 2, 3), (4, 3, 2, 1), (4, 11, 20, 14, 8, 3)))
    )
def test_mult(f, g, fg):
    pass


@pytest.mark.parametrize(
    "a, f, af", (
     (3, (2, 1), (6, 3)),
     (-3, (2, 1), (-6, -3)),
     (-3, (2, -1), (-6, 3)))
    )
def test_mult_scalar(a, f, af):
    pass


def test_reverse_mult_scalar():
    pass

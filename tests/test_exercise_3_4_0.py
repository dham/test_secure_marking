try:
    from polynomials import Polynomial
except ImportError:
    pass
import pytest


def test_import():
    pass


def test_equality():
    pass


@pytest.mark.parametrize(
    "a, b, sum",
    (((0,), (0, 1), (0, 1)),
     ((2, 0, 3), (1, 2), (3, 2, 3)),
     ((4, 2), (10, 2, 4), (14, 4, 4)))
    )
def test_add(a, b, sum):
    pass


def test_add_scalar():
    pass


def test_reverse_add_scalar():
    pass


def test_add_unknown():
    pass

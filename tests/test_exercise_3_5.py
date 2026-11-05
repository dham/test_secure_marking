try:
    from polynomials import Polynomial
except ImportError:
    pass
import pytest


class SpikedError(Exception):
    '''A dummy error just for the purpose of testing.'''
    pass


@pytest.mark.parametrize(
    "f, g", (
        ((3, 2, 1), (2, 2)),
        ((-6, -11, 3, 2, 1), (-11, 6, 6, 4)),
        ((1, 1), (1,)),
        ((1,), (0,))
    )
)
def test_dx(f, g):
    pass


def test_derivative_exists():
    pass


def test_derivative_calls_dx():
    pass

@pytest.mark.parametrize(
    "f, g", (
        ((3, 2, 1), (2, 2)),
        ((-6, -11, 3, 2, 1), (-11, 6, 6, 4)),
        ((1, 1), (1,)),
        ((1,), (0,))
    )
)
def test_derivative(f, g):
    pass

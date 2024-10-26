"""Tests the add something Module."""

import pytest

from my_project.sub_package.add_something import add_both


@pytest.mark.parametrize(
    (
        "a",
        "b",
        "expected",
    ),
    [(1, 2, 3), (2, 4, 6), (4, 5, 9)],
)
def test_add_both(a: float, b: float, expected: float):
    """Test for the add both function.

    Should add two numbers.
    """
    a = 1
    b = 2
    c = add_both(a, b)
    assert c == 3

"""Tests the add something Module."""

from my_project.sub_package.add_something import add_both


def test_add_both():
    """First test."""
    a = 1
    b = 2
    c = add_both(a, b)
    assert c == 3


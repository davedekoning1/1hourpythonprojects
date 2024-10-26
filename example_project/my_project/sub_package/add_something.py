"""Module to add two numbers."""


def add_both(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    :param a: first number
    :type a: float
    :param b: second number
    :type b: float
    :return: result
    :rtype: float
    """
    return a + b


def add_any(values: list) -> float:
    """
    Add all numbers from the list.

    :param values: list with values
    :type values: list
    :return: sum of all values
    :rtype: float
    """
    return sum(values)

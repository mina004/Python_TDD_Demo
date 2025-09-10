
# src/simple_math/core.py

from __future__ import annotations


def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.

    Examples:
        >>> add(2.0, 3.5)
        5.5
    """
    return a + b


def safe_divide(a: float, b: float) -> float:
    """
    Return a / b. Raise ValueError if b == 0.0.

    Examples:
        >>> safe_divide(10.0, 2.0)
        5.0
        >>> safe_divide(1.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: division by zero
    """
    if b == 0.0:
        raise ValueError("denominator must not be zero")
    return a / b


def sqrt_approx(x: float, iterations: int = 12) -> float:
    """
    Approximate sqrt(x) using Newton's method.
    Raise ValueError if x < 0.0.

    Notes:
        - Handles x == 0.0 quickly.
        - Uses a reasonable initial guess and 'iterations' refinement steps.

    Examples:
        >>> round(sqrt_approx(9.0), 6)
        3.0
    """
    if x < 0.0:
        raise ValueError("cannot take sqrt of negative number")
    if x == 0.0:
        return 0.0

    # Good initial guess: x for x >= 1, else 1.0
    guess = x if x >= 1.0 else 1.0
    for _ in range(max(1, int(iterations))):
        guess = 0.5 * (guess + x / guess)
    return guess


def average(xs: list[float]) -> float:
    """
    Return arithmetic mean of xs. Raise ValueError on empty list.

    Examples:
        >>> average([1.0, 2.0, 3.0])
        2.0
    """
    if not xs:
        raise ValueError("xs must not be empty")
    return sum(xs) / len(xs)

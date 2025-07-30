#!/usr/bin/env python3
"""
Module 8-make_multiplier
This module defines a function that returns a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply with.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product.
    """
    def inner(value: float) -> float:
        """
        Multiplies a float by the multiplier provided to the outer function.

        Args:
            value (float): The number to be multiplied.

        Returns:
            float: The product of value and multiplier.
        """
        return (value * multiplier)
    return inner

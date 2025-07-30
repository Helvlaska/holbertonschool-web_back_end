#!/usr/bin/env python3
"""
Module 7-to_kv
This module defines a function that returns a tuple containing a string
and the square of a number as a float.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (int | float): A number to square.

    Returns:
        Tuple[str, float]: A tuple where the first element is k, and
        the second is v squared as a float.
    """
    return (k, v * v)

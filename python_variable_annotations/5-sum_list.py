#!/usr/bin/env python3
"""
Module 5-sum_list
This module defines a function that returns the sum of a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)

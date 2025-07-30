#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
This module defines a function that returns the sum of a list
containing integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_list (List[Union[int, float]]): The list containing
        int and float elements.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return sum(mxd_list)

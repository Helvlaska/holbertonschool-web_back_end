#!/usr/bin/env python3
"""
Module 9-element_length
This module defines a function that computes the length of each element in
an iterable of sequences.
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like elements (e.g.,
        strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list where each tuple contains an element
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

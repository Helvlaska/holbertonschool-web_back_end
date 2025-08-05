#!/usr/bin/env python3
"""Module using async comprehension to collect 10 random floats."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async
    comprehension.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]

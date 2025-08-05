#!/usr/bin/env python3
"""Module that defines a coroutine to run multiple asynchronous
tasks concurrently.

It imports the wait_random coroutine and defines wait_n, which spawns several
instances of wait_random and returns a list of delays in ascending order of
completion.
"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times concurrently with the given max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value passed to wait_random.

    Returns:
        List[float]: A list of all delays in ascending order of completion.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

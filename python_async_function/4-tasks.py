#!/usr/bin/env python3
"""Module that launches multiple asyncio Tasks and returns their
results in order of completion."""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Run task_wait_random n times and return the list of delays
    as they complete.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        list[float]: Delays in ascending order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays

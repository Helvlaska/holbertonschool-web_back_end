#!/usr/bin/env python3
"""This module contains an asynchronous coroutine that waits for a
random delay.

It defines the function `wait_random` which pauses the execution for a randomly
generated duration between 0 and a specified maximum delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (included) and
    return it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

#!/usr/bin/env python3
"""Module that returns an asyncio Task for wait_random coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task for wait_random with given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A scheduled task wrapping wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))

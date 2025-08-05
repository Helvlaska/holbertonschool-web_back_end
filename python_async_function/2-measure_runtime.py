#!/usr/bin/env python3
"""Module to measure the average execution time of wait_n coroutine."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure total runtime for wait_n and return average time per call.

    Args:
        n (int): Number of wait_random calls to run concurrently.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: Average time per call (total_time / n).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

#!/usr/bin/env python3
"""Python async comprehension"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns time wasted"""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    e = time.perf_counter()
    return e - s

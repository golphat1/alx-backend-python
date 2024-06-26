#!/usr/bin/env python3
""" task_wait_random that takes an integer
max_delay and returns a asyncio.Tas """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
        Args:
            max_delay: max wait

        Return:
            Task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task

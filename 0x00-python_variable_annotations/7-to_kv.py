#!/usr/bin/env python3
"""
Complex annotated-type function - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    cast to tuple
    """
    return (k, v**2)

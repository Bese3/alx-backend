#!/usr/bin/env python3
"""computing index range"""
from typing import Tuple


def index_range(page:int, page_size: int) -> Tuple:
    """
    The function `index_range` calculates the starting and
    ending indices for a given page and page size.
    """
    return ((page - 1) * page_size, page * page_size)

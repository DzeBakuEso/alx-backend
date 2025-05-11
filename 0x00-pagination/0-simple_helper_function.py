#!/usr/bin/env python3
"""
This module provides a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start and end index for pagination.

    Args:
        page (int): the current page number (1-indexed)
        page_size (int): the number of items per page

    Returns:
        tuple: (start index, end index) for the items on the current page
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)

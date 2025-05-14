#!/usr/bin/env python3
"""FIFO caching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Add item to cache using FIFO algorithm
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data and
                len(self.cache_data) >= self.MAX_ITEMS):
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get item from cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

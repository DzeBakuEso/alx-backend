#!/usr/bin/env python3
"""LIFO caching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add item to cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data and
                len(self.cache_data) >= self.MAX_ITEMS):
            # Discard the most recently added item (last key used)
            if self.last_key is not None:
                print("DISCARD:", self.last_key)
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get item from cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

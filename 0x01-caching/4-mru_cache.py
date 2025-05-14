#!/usr/bin/env python3
"""MRU caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A MRU caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Add item to cache using MRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove and reinsert to mark it as the most recently used
            del self.cache_data[key]

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = next(reversed(self.cache_data))
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get item from cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

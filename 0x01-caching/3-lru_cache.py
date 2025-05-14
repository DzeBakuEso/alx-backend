#!/usr/bin/env python3
"""LRU caching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A LRU caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Add item to cache using LRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move item to the end to mark it as recently used
            del self.cache_data[key]

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = next(iter(self.cache_data))
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

        self.cache_data[key] = item

    def get(self, key):
        """Get item from cache by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

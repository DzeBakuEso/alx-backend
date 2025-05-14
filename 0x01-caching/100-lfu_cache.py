#!/usr/bin/env python3
"""LFU caching module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A LFU caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        self.cache_freq = {}

    def put(self, key, item):
        """Add item to cache using LFU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least frequently used item
            lfu_key = self._get_lfu_key()
            print(f"DISCARD: {lfu_key}")
            del self.cache_data[lfu_key]
            del self.cache_freq[lfu_key]

        self.cache_data[key] = item
        self.cache_freq[key] = self.cache_freq.get(key, 0) + 1

    def get(self, key):
        """Get item from cache by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_freq[key] += 1
        return self.cache_data[key]

    def _get_lfu_key(self):
        """Get the least frequently used key"""
        return min(self.cache_freq, key=self.cache_freq.get)

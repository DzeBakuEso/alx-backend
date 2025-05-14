#!/usr/bin/env python3
"""Basic caching module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system that inherits from BaseCaching.
    No limit on the number of items stored.
    """

    def put(self, key, item):
        """Assign an item to the cache using the key.

        Args:
            key (str): The key under which to store the item.
            item (Any): The item to store.

        If either key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            The cached item, or None if key is None or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

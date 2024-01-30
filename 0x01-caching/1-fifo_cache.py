#!/usr/bin/env python3
"""
FIFO cache implementing class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    The `FIFOCache` class is a cache implementation that uses the
    First-In-First-Out (FIFO) eviction policy.
    """
    def __init__(self):
        """
        The above function is the constructor method for a class.
        """
        super().__init__()

    def put(self, key, item):
        """
        The function `put` adds a key-value pair to a cache,
        and if the cache is full, it removes the
        oldest item before adding the new item.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            for i in self.cache_data.keys():
                del self.cache_data[i]
                print(f"DISCARD: {i}")
                break
        self.cache_data[key] = item

    def get(self, key):
        """
        The function retrieves the value associated with a given
        key from a cache data structure.
        """
        value = None
        if key is None:
            return None
        try:
            value = self.cache_data.get(key)
        except KeyError:
            pass
        return value

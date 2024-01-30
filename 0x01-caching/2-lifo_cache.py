#!/usr/bin/env python3
"""
FIFO cache implementing class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    The `LIFOCache` class is a cache implementation that uses the
    Last-In-First-Out (LIFO) eviction policy.
    """
    __last_key = ""

    def __init__(self):
        """
        The above function is the constructor method for a class.
        """
        super().__init__()

    def put(self, key, item):
        """
        The function `put` adds a key-value pair to a cache,
        and if the cache is full, it removes the
        newest item before adding the new item.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data.keys():
            last_key = LIFOCache.__last_key
            self.cache_data.pop(last_key, None)
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        LIFOCache.__last_key = key

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

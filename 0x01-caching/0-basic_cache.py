#!/usr/bin/env python3
"""
basic caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    The above class isimplementing basic caching.
    """
    def __init__(self):
        """
        The above function is the constructor method for a class.
        """
        super().__init__()

    def put(self, key, item):
        """
        The function stores an item in a cache data structure using
        a key-value pair.
        """
        if key is None or item is None:
            return
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

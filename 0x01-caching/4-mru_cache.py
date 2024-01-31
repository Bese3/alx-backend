#!/usr/bin/env python3
"""
MRU cache implementing class
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    The `MRUCache` class is a cache implementation that uses the
    Most-Recently-Used (MRU) eviction policy.
    """

    def __init__(self):
        """
        The above function is the constructor method for a class.
        """
        super().__init__()
        self.recent_time = {}

    def put(self, key, item):
        """
        The function `put` adds a key-value pair to a cache,
        and if the cache is full, it removes the
        MRU item before adding the new item.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data.keys():
            lowest = sorted(self.recent_time.values())[0]
            my_key = ""
            for k, v in self.recent_time.items():
                if v > lowest:
                    lowest = v
                    my_key = k
                # print(my_key)
            self.cache_data.pop(my_key, None)
            self.recent_time.pop(my_key, None)
            print(f"DISCARD: {my_key}")

        self.cache_data[key] = item
        if len(self.recent_time.values()) == 0:
            self.recent_time[key] = 0
        else:
            self.recent_time[key] = sorted(self.recent_time.values())[-1] + 1
        # self.recent_time[key] = 1
        # print(f"recent time = {self.recent_time}")

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
            if key in self.recent_time.keys():
                last_value = sorted(self.recent_time.values())[-1] + 1
                self.recent_time[key] = last_value
        except KeyError:
            pass
        return value

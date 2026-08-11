# -*- coding: utf-8 -*-


class GraphCacheEngine:

    def __init__(self):

        self.cache = {}

    def set(self, key, value):

        self.cache[key] = value

        return True

    def get(self, key):

        return self.cache.get(key)

    def exists(self, key):

        return key in self.cache

    def delete(self, key):

        if key in self.cache:
            del self.cache[key]
            return True

        return False

    def clear(self):

        self.cache.clear()

        return True

    def info(self):

        return {
            "engine": "Graph Cache Engine",
            "version": "1.0",
            "items": len(self.cache),
        }

# -*- coding: utf-8 -*-


class ArticleCacheEngine:
    """
    محرك التخزين المؤقت للمقالات.
    """

    def __init__(self):
        self._cache = {}

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value

    def has(self, key):
        return key in self._cache

    def clear(self):
        self._cache.clear()

    def info(self):
        return {
            "engine": "Article Cache Engine",
            "version": "1.0",
            "status": "production",
            "cached_items": len(self._cache),
        }

# -*- coding: utf-8 -*-


class ProviderCacheEngine:

    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        self.cache[key] = value
        return True

    def get(self, key):
        return self.cache.get(key)

    def info(self):
        return {
            "engine": "Provider Cache Engine",
            "version": "1.0",
            "items": len(self.cache),
        }

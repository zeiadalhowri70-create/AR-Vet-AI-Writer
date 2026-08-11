# -*- coding: utf-8 -*-


class BloggerDuplicateGuardEngine:

    VERSION = "1.0"

    def __init__(self):

        self.cache = set()

    def check(self, article):

        key = article.get("title", "") + str(len(article.get("html", "")))

        if key in self.cache:

            return {"duplicate": True, "key": key}

        self.cache.add(key)

        return {"duplicate": False, "key": key}

    def info(self):

        return {
            "engine": "Blogger Duplicate Guard Engine",
            "version": self.VERSION,
            "status": "production",
        }

# -*- coding: utf-8 -*-


class BloggerContentSafetyEngine:

    VERSION = "1.0"

    def check(self, article):

        html = article.get("html", "").lower()

        blocked = ["malware", "hack", "illegal"]

        found = [x for x in blocked if x in html]

        return {
            "safe": len(found) == 0,
            "blocked_terms": found,
            "engine": "Blogger Content Safety Engine",
            "version": self.VERSION,
        }

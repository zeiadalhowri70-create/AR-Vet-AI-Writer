# -*- coding: utf-8 -*-


class BloggerQualityGateEngine:

    VERSION = "1.0"

    def check(self, article):

        errors = []

        title = article.get("title", "")
        html = article.get("html", "")

        if len(title) < 10:
            errors.append("weak_title")

        if len(html) < 1000:
            errors.append("weak_content")

        score = max(0, 100 - (len(errors) * 25))

        return {
            "passed": len(errors) == 0,
            "score": score,
            "errors": errors,
            "engine": "Blogger Quality Gate Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Quality Gate Engine",
            "version": self.VERSION,
            "status": "production",
        }

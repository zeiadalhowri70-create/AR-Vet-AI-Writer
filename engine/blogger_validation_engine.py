# -*- coding: utf-8 -*-


class BloggerValidationEngine:

    VERSION = "1.0"

    def validate(self, article):

        errors = []

        if not isinstance(article, dict):
            errors.append("article_not_dict")
            return self.result(errors)

        if not article.get("title"):
            errors.append("missing_title")

        if not article.get("html"):
            errors.append("missing_html")

        if len(article.get("html", "")) < 500:
            errors.append("html_too_short")

        return self.result(errors)

    def result(self, errors):

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "engine": "Blogger Validation Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Validation Engine",
            "version": self.VERSION,
            "status": "production",
        }

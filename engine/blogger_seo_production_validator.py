# -*- coding: utf-8 -*-


class BloggerSEOProductionValidator:

    VERSION = "1.0"

    def validate(self, article):

        errors = []

        title = article.get("title", "")
        html = article.get("html", "")

        if len(title) < 10:
            errors.append("title_too_short")

        if len(html) < 1000:
            errors.append("content_too_short")

        if not article.get("labels"):
            errors.append("missing_labels")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "engine": "Blogger SEO Production Validator",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger SEO Production Validator",
            "version": self.VERSION,
            "status": "production",
        }

# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Publishing Readiness Engine

Production Validation Layer
Stage: Publishing Intelligence v2.0
"""


class ArticlePublishingReadinessEngine:

    VERSION = "2.0"

    def __init__(self):
        pass

    def _check_html(self, article):

        html = article.get("html", "")

        if not html:
            return False

        required = [
            "<html",
            "<title>",
            "<h2",
        ]

        return all(item in html for item in required)

    def _check_seo(self, article):

        seo = article.get("seo_meta") or article.get("metadata") or {}

        if not isinstance(seo, dict):
            return False

        return bool(seo.get("title") or seo.get("description"))

    def _check_schema(self, article):

        schema = article.get("schema")

        if isinstance(schema, dict):
            return bool(
                schema.get("type") or schema.get("@type") or schema.get("headline")
            )

        html = article.get("html", "")

        return "application/ld+json" in html

    def _check_references(self, article):

        references = article.get("references", [])

        return isinstance(references, list) and len(references) > 0

    def _check_images(self, article):

        image = article.get("image")

        if isinstance(image, dict):

            return bool(
                image.get("valid")
                or image.get("featured_ready")
                or image.get("seo_ready")
            )

        html = article.get("html", "")

        return "img" in html

    def check(self, article):

        checks = {
            "html": self._check_html(article),
            "seo_meta": self._check_seo(article),
            "schema": self._check_schema(article),
            "references": self._check_references(article),
            "quality_score": bool(article.get("quality_score")),
            "final_review": bool(article.get("final_review")),
            "images": self._check_images(article),
        }

        blocking_issues = [key for key, value in checks.items() if not value]

        passed = sum(1 for value in checks.values() if value)

        total = len(checks)

        score = int((passed / total) * 100)

        ready = len(blocking_issues) == 0

        return {
            "ready": ready,
            "score": score,
            "checks": checks,
            "blocking_issues": blocking_issues,
            "status": ("ready_to_publish" if ready else "needs_fix"),
        }

    def info(self):

        return {
            "engine": "Article Publishing Readiness Engine",
            "version": self.VERSION,
            "status": "production",
        }

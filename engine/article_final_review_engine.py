# -*- coding: utf-8 -*-


class ArticleFinalReviewEngine:
    """
    يراجع المقال النهائي قبل الإخراج.
    """

    def __init__(self):
        self.version = "1.0"

    def review(self, article):
        checks = {
            "html": bool(article.get("html")),
            "seo": bool(article.get("seo_meta")),
            "schema": bool(article.get("schema")),
            "references": bool(article.get("references")),
            "quality_score": bool(article.get("quality_score")),
            "related_articles": bool(article.get("related_articles_html")),
            "navigation": bool(article.get("navigation_html")),
        }

        passed = sum(1 for value in checks.values() if value)

        total = len(checks)

        score = int((passed / total) * 100)

        warnings = [name for name, value in checks.items() if not value]

        return {
            "score": score,
            "checks": checks,
            "warnings": warnings,
            "status": "passed" if score >= 85 else "needs_review",
        }

    def info(self):
        return {
            "engine": "Article Final Review Engine",
            "version": self.version,
            "status": "production",
        }

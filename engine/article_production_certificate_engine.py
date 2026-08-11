# -*- coding: utf-8 -*-

from datetime import datetime, timezone


class ArticleProductionCertificateEngine:
    """
    محرك شهادة إنتاج المقال.
    """

    def generate(self, article):
        return {
            "certificate_version": "1.0",
            "article_title": article.get("title", ""),
            "issued_at": datetime.now(timezone.utc).isoformat(),
            "status": "certified",
            "pipeline_version": "6.9",
        }

    def info(self):
        return {
            "engine": "Article Production Certificate Engine",
            "version": "1.0",
            "status": "production",
        }

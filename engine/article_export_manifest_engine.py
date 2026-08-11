# -*- coding: utf-8 -*-


class ArticleExportManifestEngine:
    """
    ينشئ Manifest نهائي للمقال قبل التصدير.
    """

    def generate(self, article):

        return {
            "title": article.get("title", ""),
            "version": "1.0",
            "ready": True,
            "exports": article.get("export", {}),
            "has_metadata": "metadata" in article,
            "has_seo": "seo" in article,
            "has_statistics": "statistics" in article,
            "has_validation": "validation" in article,
            "has_integrity": "integrity" in article,
        }

    def info(self):
        return {
            "engine": "Article Export Manifest Engine",
            "version": "1.0",
            "status": "production",
        }

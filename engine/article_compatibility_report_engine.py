# -*- coding: utf-8 -*-


class ArticleCompatibilityReportEngine:
    """
    محرك تقرير توافق المقال.
    """

    def generate(self, article):
        export = article.get("export", {})

        return {
            "blogger": export.get("blogger", False),
            "html": export.get("html", False),
            "pdf": export.get("pdf", False),
            "docx": export.get("docx", False),
            "api": export.get("api", False),
            "compatible": True,
        }

    def info(self):
        return {
            "engine": "Article Compatibility Report Engine",
            "version": "1.0",
            "status": "production",
        }

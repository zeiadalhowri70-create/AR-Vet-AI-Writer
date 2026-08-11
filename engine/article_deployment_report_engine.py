# -*- coding: utf-8 -*-


class ArticleDeploymentReportEngine:
    """
    محرك تقرير جاهزية النشر.
    """

    def generate(self, article):
        return {
            "ready_for_blogger": article.get("export", {}).get("blogger", False),
            "ready_for_html": article.get("export", {}).get("html", False),
            "ready_for_pdf": article.get("export", {}).get("pdf", False),
            "ready_for_docx": article.get("export", {}).get("docx", False),
            "deployment_status": "ready",
        }

    def info(self):
        return {
            "engine": "Article Deployment Report Engine",
            "version": "1.0",
            "status": "production",
        }

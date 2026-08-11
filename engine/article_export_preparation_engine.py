# -*- coding: utf-8 -*-


class ArticleExportPreparationEngine:
    """
    تجهيز المقال للتصدير النهائي.
    """

    def prepare(self, article):

        exported = dict(article)

        exported["export"] = {
            "html": True,
            "blogger": True,
            "pdf": False,
            "docx": False,
            "api": False,
        }

        exported["export_version"] = "1.0"

        return exported

    def info(self):
        return {
            "engine": "Article Export Preparation Engine",
            "version": "1.0",
            "status": "production",
        }

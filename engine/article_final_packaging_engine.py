# -*- coding: utf-8 -*-
from engine.article_export_package_engine import ArticleExportPackageEngine


class ArticleFinalPackagingEngine:
    """
    تجهيز الحزمة النهائية للمقال قبل مرحلة التصدير أو النشر.
    """

    def __init__(self):
        self.export_package = ArticleExportPackageEngine()

    def package(self, article):

        package = dict(article)

        package["ready_for_export"] = True
        package["package_version"] = "1.0"

        package.setdefault("metadata", {})
        package.setdefault("seo", {})
        package.setdefault("statistics", {})
        package.setdefault("validation", {})

        package["export_package"] = self.export_package.build(package)

        return package

    def info(self):
        return {
            "engine": "Article Final Packaging Engine",
            "version": "2.0",
            "status": "production",
        }

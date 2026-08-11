# -*- coding: utf-8 -*-


class ArticleIntegrityEngine:
    """
    التحقق من سلامة بنية المقال قبل التصدير النهائي.
    """

    REQUIRED_KEYS = ["metadata", "seo", "statistics", "validation"]

    def check(self, article):

        missing = []

        for key in self.REQUIRED_KEYS:
            if key not in article:
                missing.append(key)

        return {"passed": len(missing) == 0, "missing": missing}

    def info(self):
        return {
            "engine": "Article Integrity Engine",
            "version": "1.0",
            "status": "production",
        }

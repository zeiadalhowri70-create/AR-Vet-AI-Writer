# -*- coding: utf-8 -*-


class ArticleHealthMonitorEngine:
    """
    محرك مراقبة سلامة إنتاج المقال.
    """

    REQUIRED = (
        "metadata",
        "seo",
        "statistics",
        "validation",
        "integrity",
        "export",
    )

    def check(self, article):
        missing = [key for key in self.REQUIRED if key not in article]

        return {"healthy": len(missing) == 0, "missing": missing}

    def info(self):
        return {
            "engine": "Article Health Monitor Engine",
            "version": "1.0",
            "status": "production",
        }

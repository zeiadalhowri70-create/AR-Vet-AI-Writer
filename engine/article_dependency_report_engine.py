# -*- coding: utf-8 -*-


class ArticleDependencyReportEngine:
    """
    محرك تقرير مكونات إنتاج المقال.
    """

    def generate(self, article):
        dependencies = []

        mapping = {
            "metadata": "ArticleMetadataEngine",
            "seo": "ArticleSEOEnhancementEngine",
            "statistics": "ArticleStatisticsEngine",
            "validation": "ArticleValidationEngine",
            "integrity": "ArticleIntegrityEngine",
            "export": "ArticleExportPreparationEngine",
            "health": "ArticleHealthMonitorEngine",
            "runtime": "ArticleRuntimeContextEngine",
        }

        for key, engine in mapping.items():
            if key in article:
                dependencies.append(engine)

        return {"engines": dependencies, "count": len(dependencies)}

    def info(self):
        return {
            "engine": "Article Dependency Report Engine",
            "version": "1.0",
            "status": "production",
        }

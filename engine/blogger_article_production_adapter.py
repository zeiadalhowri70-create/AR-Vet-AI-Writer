# -*- coding: utf-8 -*-


from engine.blogger_seo_production_validator import BloggerSEOProductionValidator


class BloggerArticleProductionAdapter:

    VERSION = "1.0"

    def __init__(self):

        self.seo = BloggerSEOProductionValidator()

    def prepare(self, article):

        validation = self.seo.validate(article)

        return {
            "article": article,
            "seo_validation": validation,
            "ready": validation["valid"],
            "valid": validation["valid"],
            "engine": "Blogger Article Production Adapter",
            "version": self.VERSION,
        }

    def process(self, article):
        """
        Backward compatibility wrapper.
        """
        return self.prepare(article)

    def info(self):

        return {
            "engine": "Blogger Article Production Adapter",
            "version": self.VERSION,
            "status": "production",
        }

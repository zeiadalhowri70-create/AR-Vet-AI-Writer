# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production SEO Pipeline Manager

Full SEO assembly workflow.
"""


class SEOPipelineManager:

    VERSION = "1.1.0"

    def __init__(
        self,
        metadata_adapter=None,
        schema_adapter=None,
        faq_adapter=None,
        links_adapter=None,
    ):

        self.metadata = metadata_adapter
        self.schema = schema_adapter
        self.faq = faq_adapter
        self.links = links_adapter

    def build(self, article):

        package = {"article": article, "version": self.VERSION, "seo": {}}

        if self.metadata:
            package["seo"]["metadata"] = self.metadata.generate(article)

        if self.schema:
            package["seo"]["schema"] = self.schema.generate(article)

        if self.faq:
            package["seo"]["faq"] = self.faq.generate(article)

        if self.links:
            package["seo"]["links"] = self.links.generate(article)

        return package

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "metadata": self.metadata is not None,
            "schema": self.schema is not None,
            "faq": self.faq is not None,
            "links": self.links is not None,
        }


if __name__ == "__main__":

    manager = SEOPipelineManager()

    print(manager.health())

    print(manager.build("مرض النيوكاسل في الدواجن"))

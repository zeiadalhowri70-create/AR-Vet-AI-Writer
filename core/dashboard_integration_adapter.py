# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production Dashboard Integration Adapter
"""


class DashboardIntegrationAdapter:

    VERSION = "1.0.0"

    def __init__(
        self,
        article_engine=None,
        blogger_engine=None,
        media_engine=None,
        analytics_engine=None,
        seo_engine=None,
    ):

        self.article_engine = article_engine
        self.blogger_engine = blogger_engine
        self.media_engine = media_engine
        self.analytics_engine = analytics_engine
        self.seo_engine = seo_engine

    def collect(self):

        return {
            "articles": self.article_engine is not None,
            "publishing": self.blogger_engine is not None,
            "media": self.media_engine is not None,
            "analytics": self.analytics_engine is not None,
            "seo": self.seo_engine is not None,
            "version": self.VERSION,
        }

    def health(self):

        return {"status": True, "version": self.VERSION}


if __name__ == "__main__":

    adapter = DashboardIntegrationAdapter()

    print(adapter.health())

    print(adapter.collect())

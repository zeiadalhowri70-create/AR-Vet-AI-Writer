# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production Analytics Pipeline Manager

Responsible for:
- Analytics adapters management
- Metrics collection
- Reporting package creation
"""

from datetime import datetime


class AnalyticsPipelineManager:

    VERSION = "1.0.0"

    def __init__(
        self, search_console=None, ga4=None, blogger=None, ranking=None, ctr=None
    ):

        self.search_console = search_console
        self.ga4 = ga4
        self.blogger = blogger
        self.ranking = ranking
        self.ctr = ctr

    def collect(self, article=None):

        package = {
            "article": article,
            "version": self.VERSION,
            "timestamp": datetime.utcnow().isoformat(),
            "analytics": {},
        }

        if self.search_console:
            package["analytics"]["search_console"] = self.search_console.collect(
                article
            )

        if self.ga4:
            package["analytics"]["ga4"] = self.ga4.collect(article)

        if self.blogger:
            package["analytics"]["blogger"] = self.blogger.collect(article)

        if self.ranking:
            package["analytics"]["ranking"] = self.ranking.collect(article)

        if self.ctr:
            package["analytics"]["ctr"] = self.ctr.collect(article)

        return package

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "search_console": self.search_console is not None,
            "ga4": self.ga4 is not None,
            "blogger": self.blogger is not None,
            "ranking": self.ranking is not None,
            "ctr": self.ctr is not None,
        }


if __name__ == "__main__":

    manager = AnalyticsPipelineManager()

    print(manager.health())

    print(manager.collect("مرض النيوكاسل في الدواجن"))

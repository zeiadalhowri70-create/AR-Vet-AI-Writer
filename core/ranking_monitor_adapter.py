# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production Ranking Monitor Adapter
"""


class RankingMonitorAdapter:

    VERSION = "1.0.0"

    def __init__(self, api=None):
        self.api = api

    def authenticate(self):

        return {"authenticated": self.api is not None, "platform": "ranking_monitor"}

    def collect(self, article=None):

        if not self.api:
            return {
                "status": False,
                "platform": "ranking_monitor",
                "error": "Ranking Monitor API unavailable",
                "article": article,
            }

        return self.api.collect(article)

    def health(self):

        return {
            "status": True,
            "platform": "ranking_monitor",
            "version": self.VERSION,
            "api_connected": self.api is not None,
        }


if __name__ == "__main__":

    adapter = RankingMonitorAdapter()

    print(adapter.health())

    print(adapter.collect("مرض النيوكاسل في الدواجن"))

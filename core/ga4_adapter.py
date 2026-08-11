# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production Google Analytics 4 Adapter
"""


class GA4Adapter:

    VERSION = "1.0.0"

    def __init__(self, api=None):
        self.api = api

    def authenticate(self):

        return {"authenticated": self.api is not None, "platform": "ga4"}

    def collect(self, article=None):

        if not self.api:
            return {
                "status": False,
                "platform": "ga4",
                "error": "GA4 API unavailable",
                "article": article,
            }

        return self.api.collect(article)

    def health(self):

        return {
            "status": True,
            "platform": "ga4",
            "version": self.VERSION,
            "api_connected": self.api is not None,
        }


if __name__ == "__main__":

    adapter = GA4Adapter()

    print(adapter.health())

    print(adapter.collect("مرض النيوكاسل في الدواجن"))

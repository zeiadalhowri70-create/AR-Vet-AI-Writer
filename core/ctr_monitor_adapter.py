# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Production CTR Monitor Adapter
"""


class CTRMonitorAdapter:

    VERSION = "1.0.0"

    def __init__(self, api=None):
        self.api = api

    def authenticate(self):

        return {"authenticated": self.api is not None, "platform": "ctr_monitor"}

    def collect(self, article=None):

        if not self.api:
            return {
                "status": False,
                "platform": "ctr_monitor",
                "error": "CTR Monitor API unavailable",
                "article": article,
            }

        return self.api.collect(article)

    def health(self):

        return {
            "status": True,
            "platform": "ctr_monitor",
            "version": self.VERSION,
            "api_connected": self.api is not None,
        }


if __name__ == "__main__":

    adapter = CTRMonitorAdapter()

    print(adapter.health())

    print(adapter.collect("مرض النيوكاسل في الدواجن"))

# -*- coding: utf-8 -*-


class ProviderRateLimitEngine:

    def limit(self):

        return {"requests_per_minute": 60, "enabled": True}

    def info(self):
        return {"engine": "Provider Rate Limit Engine", "version": "1.0"}

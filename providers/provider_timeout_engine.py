# -*- coding: utf-8 -*-


class ProviderTimeoutEngine:

    def timeout(self):

        return {"seconds": 60, "enabled": True}

    def info(self):
        return {"engine": "Provider Timeout Engine", "version": "1.0"}

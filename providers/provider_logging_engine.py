# -*- coding: utf-8 -*-


class ProviderLoggingEngine:

    def log(self, provider, action):

        return {"provider": provider, "action": action, "logged": True}

    def info(self):

        return {"engine": "Provider Logging Engine", "version": "1.0"}

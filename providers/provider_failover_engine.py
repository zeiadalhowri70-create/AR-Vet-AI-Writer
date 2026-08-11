# -*- coding: utf-8 -*-


class ProviderFailoverEngine:

    def failover(self, providers):

        return {
            "primary": providers[0] if providers else None,
            "secondary": providers[1] if len(providers) > 1 else None,
            "enabled": True,
        }

    def info(self):

        return {"engine": "Provider Failover Engine", "version": "1.0"}

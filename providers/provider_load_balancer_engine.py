# -*- coding: utf-8 -*-


class ProviderLoadBalancerEngine:

    def balance(self, providers):

        return {
            "selected": providers[0] if providers else None,
            "strategy": "round_robin",
        }

    def info(self):

        return {"engine": "Provider Load Balancer Engine", "version": "1.0"}

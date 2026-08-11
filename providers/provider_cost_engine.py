# -*- coding: utf-8 -*-


class ProviderCostEngine:

    def estimate(self, tokens):

        return {"tokens": tokens, "estimated_cost": round(tokens * 0.000002, 6)}

    def info(self):

        return {"engine": "Provider Cost Engine", "version": "1.0"}

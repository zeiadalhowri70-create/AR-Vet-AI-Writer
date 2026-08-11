# -*- coding: utf-8 -*-


class ProviderTokenEstimationEngine:

    def estimate(self, text):

        return {"characters": len(text), "estimated_tokens": max(1, len(text) // 4)}

    def info(self):

        return {"engine": "Provider Token Estimation Engine", "version": "1.0"}

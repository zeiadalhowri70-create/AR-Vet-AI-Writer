# -*- coding: utf-8 -*-


class ProviderPayloadEngine:

    def build(self, model, prompt):

        return {"model": model, "messages": [{"role": "user", "content": prompt}]}

    def info(self):

        return {"engine": "Provider Payload Engine", "version": "1.0"}

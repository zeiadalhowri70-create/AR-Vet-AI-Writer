# -*- coding: utf-8 -*-


class ProviderRequestEngine:

    def build(self, prompt, model=None):

        return {"prompt": prompt, "model": model, "request_ready": True}

    def info(self):

        return {"engine": "Provider Request Engine", "version": "1.0"}

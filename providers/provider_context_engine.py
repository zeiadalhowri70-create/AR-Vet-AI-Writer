# -*- coding: utf-8 -*-


class ProviderContextEngine:

    def build(self, prompt):

        return {"prompt": prompt, "context_ready": True}

    def info(self):

        return {"engine": "Provider Context Engine", "version": "1.0"}

# -*- coding: utf-8 -*-


class ProviderHeadersEngine:

    def build(self, api_key):

        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def info(self):

        return {"engine": "Provider Headers Engine", "version": "1.0"}

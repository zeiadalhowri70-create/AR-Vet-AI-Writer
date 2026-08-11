# -*- coding: utf-8 -*-


class ProviderRetryEngine:

    def retry_config(self, retries=3):

        return {"enabled": True, "max_retries": retries}

    def info(self):
        return {"engine": "Provider Retry Engine", "version": "1.0"}

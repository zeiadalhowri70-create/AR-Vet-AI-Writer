# -*- coding: utf-8 -*-


class ProviderAuthenticationEngine:

    def authenticate(self, api_key):

        return {"authenticated": bool(api_key), "method": "api_key"}

    def info(self):

        return {"engine": "Provider Authentication Engine", "version": "1.0"}

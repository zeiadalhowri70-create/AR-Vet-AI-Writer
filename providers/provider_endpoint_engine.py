# -*- coding: utf-8 -*-


class ProviderEndpointEngine:

    def endpoint(self, provider):

        endpoints = {"mock": "https://mock.local/api"}

        return endpoints.get(provider.lower())

    def info(self):

        return {"engine": "Provider Endpoint Engine", "version": "1.0"}

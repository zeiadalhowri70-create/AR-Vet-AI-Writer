# -*- coding: utf-8 -*-


class ProviderConfigurationEngine:

    def __init__(self):

        self.config = {"mock": {"enabled": True, "model": "mock-model", "timeout": 60}}

    def get(self, provider_name):

        return self.config.get(provider_name.lower())

    def set(self, provider_name, key, value):

        provider_name = provider_name.lower()

        if provider_name not in self.config:
            self.config[provider_name] = {}

        self.config[provider_name][key] = value

        return self.config[provider_name]

    def providers(self):

        return sorted(self.config.keys())

    def info(self):

        return {
            "engine": "Provider Configuration Engine",
            "version": "1.0",
            "providers": len(self.config),
        }

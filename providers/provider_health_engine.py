# -*- coding: utf-8 -*-

from providers.provider_registry import ProviderRegistry


class ProviderHealthEngine:

    def __init__(self):

        self.registry = ProviderRegistry()

    def check(self, provider_name):

        provider = self.registry.get(provider_name)

        if provider is None:
            return {"provider": provider_name, "available": False}

        return {"provider": provider_name, "available": provider.health()}

    def check_all(self):

        result = {}

        for name in self.registry.list():
            result[name] = self.check(name)

        return result

    def info(self):

        return {
            "engine": "Provider Health Engine",
            "version": "1.0",
            "providers": len(self.registry.list()),
        }

# -*- coding: utf-8 -*-

from providers.provider_factory import ProviderFactory


class ProviderSelectionEngine:

    def __init__(self):

        self.current = "groq"

    def current_provider(self):

        return self.current

    def select(self, provider_name):

        ProviderFactory.create(provider_name)

        self.current = provider_name.lower()

        return {"selected": self.current}

    def instance(self):

        return ProviderFactory.create(self.current)

    def info(self):

        return {
            "engine": "Provider Selection Engine",
            "version": "1.0",
            "current": self.current,
        }

# -*- coding: utf-8 -*-

from providers.groq_provider import GroqProvider
from providers.gemini_provider import GeminiProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.deepseek_provider import DeepSeekProvider


class ProviderRegistry:
    """
    Production Provider Registry
    AR-Vet AI Writer
    """

    def __init__(self):
        self.providers = {
            "groq": GroqProvider,
            "gemini": GeminiProvider,
            "openrouter": OpenRouterProvider,
            "deepseek": DeepSeekProvider,
        }

    def register(self, name, provider):
        self.providers[name.lower()] = provider

    def exists(self, name):
        return name.lower() in self.providers

    def list(self):
        return sorted(self.providers.keys())

    def get(self, name):
        provider = self.providers.get(name.lower())

        if provider is None:
            return None

        return provider()

    def info(self):
        return {
            "engine": "Provider Registry",
            "version": "2.0",
            "providers": self.list(),
            "status": "production",
        }

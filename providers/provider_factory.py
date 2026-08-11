# -*- coding: utf-8 -*-

from providers.groq_provider import GroqProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.gemini_provider import GeminiProvider
from providers.openai_provider import OpenAIProvider
from providers.deepseek_provider import DeepSeekProvider
from providers.cohere_provider import CohereProvider


class ProviderFactory:

    @staticmethod
    def create(provider_name=None):

        provider_name = provider_name.lower().strip()

        providers = {
            "groq": GroqProvider,
            "openrouter": OpenRouterProvider,
            "gemini": GeminiProvider,
            "openai": OpenAIProvider,
            "deepseek": DeepSeekProvider,
            "cohere": CohereProvider,
        }

        provider_class = providers.get(provider_name)

        if provider_class is None:
            raise ValueError(f"Unsupported provider: {provider_name}")

        return provider_class()

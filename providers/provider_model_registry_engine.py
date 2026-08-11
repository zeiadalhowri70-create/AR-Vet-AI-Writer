# -*- coding: utf-8 -*-


class ProviderModelRegistryEngine:

    def __init__(self):

        self.models = {"mock": ["mock-model-v1"]}

    def list_models(self, provider_name):

        return self.models.get(provider_name.lower(), [])

    def default_model(self, provider_name):

        models = self.list_models(provider_name)

        if not models:
            return None

        return models[0]

    def add_model(self, provider_name, model_name):

        provider_name = provider_name.lower()

        self.models.setdefault(provider_name, []).append(model_name)

        return self.models[provider_name]

    def info(self):

        return {
            "engine": "Provider Model Registry Engine",
            "version": "1.0",
            "providers": len(self.models),
        }

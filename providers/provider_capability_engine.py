# -*- coding: utf-8 -*-


class ProviderCapabilityEngine:

    def __init__(self):

        self.capabilities = {
            "mock": {
                "text": True,
                "image": False,
                "audio": False,
                "video": False,
                "multimodal": False,
            }
        }

    def get(self, provider_name):

        return self.capabilities.get(provider_name.lower())

    def supports(self, provider_name, capability):

        provider = self.get(provider_name)

        if not provider:
            return False

        return provider.get(capability, False)

    def info(self):

        return {
            "engine": "Provider Capability Engine",
            "version": "1.0",
            "providers": len(self.capabilities),
        }

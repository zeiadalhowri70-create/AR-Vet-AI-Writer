# -*- coding: utf-8 -*-

from providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate(self, prompt):
        return {
            "provider": "openai",
            "success": True,
            "content": None,
            "implemented": False,
        }

    def health(self):
        return True

    def info(self):
        return {"provider": "OpenAI Provider", "version": "1.0"}

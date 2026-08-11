# -*- coding: utf-8 -*-

from providers.base_provider import BaseProvider


class DeepSeekProvider(BaseProvider):

    def generate(self, prompt):
        return {
            "provider": "deepseek",
            "success": True,
            "content": None,
            "implemented": False,
        }

    def health(self):
        return True

    def info(self):
        return {"provider": "DeepSeek Provider", "version": "1.0"}

# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class MetaWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "meta",
            "content": self.provider.generate(
                f"اكتب Meta Description احترافية لمقال {topic}."
            ),
        }

    def info(self):
        return {"engine": "Meta Writer Engine", "version": "2.0", "type": "AI Powered"}

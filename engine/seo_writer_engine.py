# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class SEOWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "seo",
            "content": self.provider.generate(
                f"أنشئ بيانات SEO كاملة لمقال بعنوان {topic}."
            ),
        }

    def info(self):
        return {"engine": "SEO Writer Engine", "version": "2.0", "type": "AI Powered"}

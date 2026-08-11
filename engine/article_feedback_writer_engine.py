# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleFeedbackWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "feedback",
            "content": self.provider.generate(
                f"أنشئ نموذج ملاحظات وتحسين لمقال {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Article Feedback Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

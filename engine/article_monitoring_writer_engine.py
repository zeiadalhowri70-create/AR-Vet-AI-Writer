# -*- coding:utf-8 -*-
from providers.provider_manager import ProviderManager


class ArticleMonitoringWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "monitoring",
            "content": self.provider.generate(f"أنشئ خطة مراقبة أداء مقال {topic}."),
        }

    def info(self):
        return {
            "engine": "Article Monitoring Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

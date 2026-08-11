# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class RiskFactorWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "risk_factor",
            "content": self.provider.generate(
                f"اكتب عوامل الخطورة المرتبطة بـ {topic}."
            ),
        }

    def info(self):
        return {
            "engine": "Risk Factor Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

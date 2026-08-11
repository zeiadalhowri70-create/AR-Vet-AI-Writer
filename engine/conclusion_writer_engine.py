# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class ConclusionWriterEngine:

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        return {
            "section": "conclusion",
            "content": self.provider.generate(
                f"أنت طبيب بيطري متخصص تكتب مقالات علمية باللغة العربية الفصحى.\n\nاكتب خاتمة علمية لمقال عن {topic} تشمل:\nتلخيص أهم النقاط التي تناولها المقال،\nوالتأكيد على الأهمية الصحية والاقتصادية للمرض،\nوالتوصية بالمراجعة الدورية للطبيب البيطري،\nوالدعوة للالتزام بالبروتوكولات العلمية الحديثة.\n\nالطول: بين 300 و450 كلمة. الأسلوب: علمي مع لمسة إيجابية ختامية. الصياغة: نثر متصل بدون قوائم. لا تستخدم Markdown."
            ),
        }

    def info(self):
        return {
            "engine": "Conclusion Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

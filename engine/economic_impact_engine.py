# -*- coding: utf-8 -*-

"""
Economic Impact Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class EconomicImpactEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير في اقتصاديات الإنتاج الحيواني وصحة الدواجن.

اكتب قسم التأثير الاقتصادي Economic Impact
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- أهمية المرض الاقتصادية عالمياً.
2- الخسائر الناتجة عن النفوق.
3- تأثير المرض على النمو والإنتاج.
4- تأثيره على معامل التحويل الغذائي.
5- تكلفة العلاج والسيطرة والتحصين.
6- الخسائر غير المباشرة.
7- تأثير المرض على المزارع الصغيرة والكبيرة.
8- العلاقة بين الوقاية وتقليل الخسائر.
9- مؤشرات اقتصادية يمكن استخدامها لتقييم الضرر.

استخدم المصطلحات العربية والإنجليزية.
اكتب بأسلوب موسوعي علمي دقيق.
تجنب الحشو والتكرار.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "economic_impact",
            "engine": "EconomicImpactEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Economic Impact Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

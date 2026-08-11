# -*- coding: utf-8 -*-

"""
Immunology Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class ImmunologyEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        context_text = context if context else ""

        prompt = f"""
أنت خبير في علم المناعة البيطرية والأمراض المعدية.

اكتب قسم المناعة (Immunology)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يشمل:

1- الاستجابة المناعية الفطرية (Innate Immunity).
2- الاستجابة المناعية المكتسبة (Adaptive Immunity).
3- الخلايا المناعية الرئيسية ودورها.
4- الأجسام المضادة Antibodies وأنواعها.
5- السيتوكينات والوسطاء الالتهابيين Cytokines.
6- تأثير العامل الممرض على الجهاز المناعي.
7- آليات الهروب المناعي Immune Evasion.
8- تكوين الذاكرة المناعية.
9- العلاقة بين المناعة والحماية الناتجة عن التحصين.

استخدم المصطلحات العربية والإنجليزية بين الأقواس.
اكتب بأسلوب موسوعة طبية بيطرية علمية دقيقة.
تجنب الحشو والتكرار.
"""

        if context_text:
            prompt += f"""

السياق العلمي:
{context_text}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "immunology",
            "engine": "ImmunologyEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Immunology Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

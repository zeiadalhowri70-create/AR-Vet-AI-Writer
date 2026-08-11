# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Abstract Engine

Production Final v1.0.0
Encyclopedia Scientific Engine
"""

from providers.provider_manager import ProviderManager


class AbstractEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير في الطب البيطري وكتابة الموسوعات العلمية.

اكتب الملخص العلمي (Scientific Abstract)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يتضمن:

1- تعريف مختصر ودقيق بالمرض.
2- أهمية المرض البيطرية والاقتصادية.
3- العامل المسبب.
4- أهم آليات الإمراضية.
5- الأعراض والآفات الرئيسية.
6- طرق التشخيص الحديثة.
7- استراتيجيات الوقاية والمكافحة.

اكتب بأسلوب موسوعي علمي.
استخدم المصطلحات العربية مع الإنجليزية بين الأقواس.
تجنب الحشو والتكرار.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "abstract",
            "engine": "AbstractEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Abstract Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

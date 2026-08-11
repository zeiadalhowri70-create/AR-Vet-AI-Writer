# -*- coding: utf-8 -*-

"""
Pathogenesis Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class PathogenesisEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        context_text = context if context else ""

        prompt = f"""
أنت أستاذ متخصص في علم الأمراض والفيروسات البيطرية.

اكتب قسم الإمراضية (Pathogenesis) لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يكون المحتوى علمياً عميقاً ومنظماً ويشمل:

1- دخول العامل الممرض إلى جسم الحيوان.
2- مستقبلات الخلايا المستهدفة.
3- آلية الالتصاق والغزو الخلوي.
4- مراحل التكاثر والانتشار.
5- انتقال العامل الممرض بين الأعضاء.
6- التغيرات الفسيولوجية والكيميائية الحيوية.
7- تلف الأنسجة والخلايا.
8- دور المناعة الفطرية والمكتسبة.
9- السيتوكينات والاستجابة الالتهابية.
10- علاقة الحمل الممرض بشدة الإصابة.
11- اختلاف الإمراضية حسب العمر والسلالة والظروف البيئية.
12- ارتباط الإمراضية بالأعراض والآفات التشريحية.

استخدم المصطلحات العربية مع الإنجليزية بين الأقواس.
تجنب الحشو والتكرار.
اكتب بأسلوب مرجع طبي بيطري.
"""

        if context_text:
            prompt += f"""

السياق العلمي المتوفر:
{context_text}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "pathogenesis",
            "engine": "PathogenesisEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Pathogenesis Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

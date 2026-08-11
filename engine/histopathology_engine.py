# -*- coding: utf-8 -*-

"""
Histopathology Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class HistopathologyEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت أستاذ في علم الأمراض البيطري (Veterinary Histopathology).

اكتب قسم الأنسجة المرضية Histopathology لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- العينات المرضية المناسبة للفحص.
2- الأعضاء والأنسجة المستهدفة.
3- التغيرات المجهرية الأساسية.
4- التغيرات الخلوية والتنكس والموت الخلوي.
5- التغيرات الالتهابية والمناعية.
6- وصف الآفات تحت المجهر.
7- العلاقة بين التغيرات النسيجية والأعراض السريرية.
8- الفرق بين الإصابة الحادة والمزمنة.
9- استخدام التقنيات الحديثة مثل:
   - Immunohistochemistry
   - PCR Localization
   - Special Stains

استخدم المصطلحات العربية والإنجليزية الطبية.
اكتب بأسلوب مرجع طبي بيطري عالمي.
تجنب الحشو والتكرار.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "histopathology",
            "engine": "HistopathologyEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Histopathology Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

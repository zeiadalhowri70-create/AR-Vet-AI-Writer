# -*- coding: utf-8 -*-

"""
Clinical Signs Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class ClinicalSignsEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري استشاري متخصص في الأمراض المعدية.

اكتب قسم الأعراض السريرية Clinical Signs
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- العلامات السريرية المبكرة.
2- العلامات حسب الجهاز المتأثر:
   - الجهاز التنفسي Respiratory System
   - الجهاز الهضمي Digestive System
   - الجهاز العصبي Nervous System
3- العلامات العامة:
   - الخمول
   - فقدان الشهية
   - انخفاض الإنتاج
4- اختلاف الأعراض حسب:
   - العمر
   - شدة الإصابة
   - السلالة
   - الحالة المناعية
5- العلاقة بين الإمراضية والعلامات السريرية.
6- العلامات التي تساعد الطبيب في التشخيص الحقلي.

استخدم المصطلحات العربية والإنجليزية الطبية.
اكتب بأسلوب مرجع طبي بيطري عالمي.
تجنب التكرار والحشو.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "clinical_signs",
            "engine": "ClinicalSignsEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Clinical Signs Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

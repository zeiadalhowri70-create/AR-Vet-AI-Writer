# -*- coding: utf-8 -*-

"""
Differential Diagnosis Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class DifferentialDiagnosisEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري استشاري متخصص في التشخيص السريري والمختبري.

اكتب قسم التشخيص التفريقي Differential Diagnosis
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- الأمراض التي تتشابه مع المرض الرئيسي.
2- مقارنة الأعراض السريرية بين الأمراض.
3- مقارنة الآفات التشريحية.
4- الفروق في الاختبارات المخبرية.
5- الفروق الجزيئية والمناعية.
6- العلامات التي تساعد الطبيب على التمييز.
7- جدول مقارنة تشخيصية عند الحاجة.
8- أهمية التشخيص التفريقي في اختيار العلاج والسيطرة.

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
            "section": "differential_diagnosis",
            "engine": "DifferentialDiagnosisEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Differential Diagnosis Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

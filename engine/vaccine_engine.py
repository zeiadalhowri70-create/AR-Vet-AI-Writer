# -*- coding: utf-8 -*-

"""
Vaccine Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class VaccineEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير دولي في علم اللقاحات البيطرية والتحصين.

اكتب قسم التحصين Vaccination
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- أهمية التحصين في السيطرة على المرض.
2- أنواع اللقاحات المستخدمة:
   - Live vaccines
   - Inactivated vaccines
   - Recombinant vaccines
3- آلية عمل اللقاح وتحفيز المناعة.
4- برامج التحصين حسب العمر ونوع التربية.
5- طرق إعطاء اللقاحات.
6- تأثير الأجسام المناعية الأمية.
7- أسباب فشل التحصين.
8- عوامل نجاح برنامج التحصين.
9- تقييم الاستجابة المناعية بعد التحصين.
10- العلاقة بين الأمن الحيوي والتحصين.

استخدم المصطلحات العربية والإنجليزية الطبية.
اكتب بأسلوب مرجع بيطري عالمي.
تجنب التكرار والحشو.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "vaccination",
            "engine": "VaccineEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Vaccine Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

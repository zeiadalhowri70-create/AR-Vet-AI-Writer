# -*- coding: utf-8 -*-

"""
Biosecurity Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class BiosecurityEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير دولي في صحة الحيوان وإدارة مزارع الدواجن.

اكتب قسم الأمن الحيوي Biosecurity لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- مفهوم الأمن الحيوي وأهدافه.
2- الأمن الحيوي الخارجي External Biosecurity.
3- الأمن الحيوي الداخلي Internal Biosecurity.
4- طرق دخول وانتقال الممرضات.
5- برامج التنظيف والتطهير.
6- إدارة الحجر الصحي.
7- التحكم في حركة الأشخاص والمعدات.
8- مكافحة القوارض والحشرات.
9- إدارة مياه الشرب والعلف.
10- تقليل عوامل الإجهاد المناعي.
11- العلاقة بين الأمن الحيوي والتحصين.
12- إجراءات الطوارئ عند ظهور المرض.

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
            "section": "biosecurity",
            "engine": "BiosecurityEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):

        return {
            "engine": "Biosecurity Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
History Engine

Production Final v1.0.0
Encyclopedia Scientific Engine
"""

from providers.provider_manager import ProviderManager


class HistoryEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت مؤرخ علمي متخصص في الطب البيطري والأمراض الحيوانية.

اكتب قسم التاريخ والاكتشاف (History)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يحتوي القسم على:

1- أول وصف علمي للمرض.
2- تاريخ اكتشاف العامل المسبب.
3- العلماء أو المؤسسات العلمية المرتبطة بالاكتشاف.
4- تطور فهم المرض عبر المراحل الزمنية.
5- أهم الاكتشافات البحثية التي غيرت طرق التشخيص والسيطرة.
6- تطور اللقاحات أو وسائل المكافحة إن وجدت.
7- الوضع العلمي الحديث للمرض.

استخدم التواريخ والمصطلحات العلمية بدقة.
اكتب بأسلوب موسوعي طبي بيطري.
استخدم العربية مع المصطلحات الإنجليزية بين الأقواس.
تجنب المعلومات غير الموثقة.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "history",
            "engine": "HistoryEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "History Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

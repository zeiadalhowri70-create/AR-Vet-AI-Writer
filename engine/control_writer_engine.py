# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class ControlWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        prompt = f"""
أنت طبيب بيطري متخصص تكتب مقالات علمية باللغة العربية الفصحى.
اكتب قسم السيطرة والتحكم في {topic} بشكل علمي ومفصل يشمل:
استراتيجيات السيطرة على المرض عند الاندلاع،
وبروتوكولات الحجر الصحي والعزل الفوري،
والتدخلات الدوائية والعلاجية الجماعية،
والتنسيق مع السلطات البيطرية الرسمية،
ومؤشرات نجاح برامج السيطرة وتقييم النتائج.

الطول: بين 600 و800 كلمة. الأسلوب: علمي رصين. الصياغة: نثر متصل بدون قوائم. لا تستخدم Markdown.
"""
        return {"section": "control", "content": self.provider.generate(prompt)}

    def info(self):
        return {
            "engine": "Control Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

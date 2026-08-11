# -*- coding: utf-8 -*-
from providers.provider_manager import ProviderManager


class PreventionWriterEngine:
    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic):
        prompt = (
            f"أنت طبيب بيطري متخصص تكتب مقالات علمية باللغة العربية الفصحى.\n"
            f"اكتب قسم الوقاية من {topic} بشكل علمي ومفصل يشمل:\n"
            "التدابير الوقائية الأساسية كالتحصين والعزل والنظافة البيطرية،\n"
            "وبرامج المراقبة والرصد الوبائي،\n"
            "والإجراءات البيوأمنية في المزارع والمرافق البيطرية،\n"
            "ودور صاحب الحيوان والمربي في الوقاية،\n"
            "والتوصيات العلمية الحديثة المعتمدة.\n"
            "الطول: بين 600 و800 كلمة. الأسلوب: علمي رصين. الصياغة: نثر متصل بدون قوائم. لا تستخدم Markdown."
        )
        return {"section": "prevention", "content": self.provider.generate(prompt)}

    def info(self):
        return {
            "engine": "Prevention Writer Engine",
            "version": "2.0",
            "type": "AI Powered",
        }

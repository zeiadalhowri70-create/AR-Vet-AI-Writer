# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class CauseWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic):

        prompt = f"""
أنت طبيب بيطري متخصص في أمراض الدواجن.

اكتب قسم "أسباب المرض" للمرض التالي:

{topic}

الشروط:

- العربية الفصحى فقط.
- بين 600 و800 كلمة.
- اذكر الأسباب والعوامل المساعدة فقط.
- اعتمد على المعلومات البيطرية المعروفة.
- لا تذكر أعراضًا أو علاجًا.
- لا تكرر الجمل.
- لا تستخدم أي لغة أجنبية.
- لا تستخدم Markdown.
- اكتب النص النهائي فقط.
"""

        return self.provider.generate(prompt)

    def info(self):

        return {
            "engine": "Cause Writer Engine",
            "version": "4.0",
            "status": "production",
        }

# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class SymptomsWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري متخصص في أمراض الدواجن.

اكتب قسم "الأعراض والعلامات السريرية" للمرض التالي:

المعلومات العلمية المساعدة من نظام AR-Vet AI:
{brain_context}



{topic}

الشروط:

- العربية الفصحى فقط.
- بين 600 و800 كلمة.
- اذكر العلامات السريرية المهمة فقط.
- فرّق بين الأعراض التنفسية والهضمية والعصبية عند الحاجة.
- لا تذكر الأسباب أو العلاج.
- لا تكرر أي جملة.
- لا تستخدم لغة أجنبية.
- لا تستخدم Markdown.
- اكتب النص النهائي فقط.
"""

        if context:
            brain = context.get("veterinary_brain", {})
            knowledge = context.get("knowledge", {})
            brain_context = f"{brain}\n{knowledge}"
        else:
            brain_context = "لا توجد بيانات إضافية."

        prompt = prompt.format(brain_context=brain_context)

        return self.provider.generate(prompt)

    def info(self):

        return {
            "engine": "Symptoms Writer Engine",
            "version": "4.0",
            "status": "production",
        }

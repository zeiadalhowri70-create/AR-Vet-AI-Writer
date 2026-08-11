# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class DiagnosisWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري متخصص في تشخيص أمراض الدواجن.

اكتب قسم "تشخيص المرض" للمرض التالي:

{topic}

المعلومات العلمية المساندة من نظام AR-Vet AI:
{brain_context}

الشروط:

- العربية الفصحى فقط.
- بين 600 و800 كلمة.
- اذكر طرق التشخيص البيطري المناسبة.
- اذكر الفحص السريري والفحوص المخبرية عند الحاجة.
- لا تذكر العلاج.
- لا تكرر الجمل.
- استخدم مصطلحات بيطرية صحيحة.
- لا تستخدم أي لغة أجنبية.
- لا تستخدم Markdown.
- اكتب النص النهائي فقط.
"""

        
        if context:
            brain = context.get("veterinary_brain", {})
            knowledge = context.get("knowledge", {})
            profile = context.get("disease_profile", {})

            brain_context = (
                f"Veterinary Brain:\n{brain}\n"
                f"Knowledge:\n{knowledge}\n"
                f"Disease Profile:\n{profile}"
            )
        else:
            brain_context = "لا توجد بيانات علمية إضافية."

        prompt = prompt.format(
            brain_context=brain_context
        )

        return self.provider.generate(prompt)


    def info(self):

        return {
            "engine": "Diagnosis Writer Engine",
            "version": "4.0",
            "status": "production",
        }

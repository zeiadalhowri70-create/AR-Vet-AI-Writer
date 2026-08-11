# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class TreatmentWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري متخصص في أمراض الدواجن.

اكتب قسم "الوقاية والسيطرة والعلاج" للمرض التالي:

{topic}

المعلومات العلمية المساندة من نظام AR-Vet AI:
{brain_context}

الشروط:

- العربية الفصحى فقط.
- بين 600 و800 كلمة.
- وضّح أنه في الأمراض الفيروسية تكون السيطرة والوقاية أهم من العلاج المباشر.
- اذكر برامج الوقاية والإجراءات الحيوية والتحصينات عند الحاجة.
- لا تقدم وصفات دوائية غير مؤكدة.
- لا تكرر الجمل.
- استخدم مصطلحات بيطرية صحيحة.
- لا تستخدم لغة أجنبية.
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
            "engine": "Treatment Writer Engine",
            "version": "4.0",
            "status": "production",
        }

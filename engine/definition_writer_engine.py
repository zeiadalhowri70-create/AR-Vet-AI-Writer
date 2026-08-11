# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class DefinitionWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic, context=None):
        knowledge = ""

        if context and isinstance(context, dict):
            profile = context.get("knowledge", {}).get("scientific_profile", {})

            if profile:
                knowledge = f"""
المعلومات العلمية المرجعية:

التعريف:
{profile.get("definition", "")}

المسبب المرضي:
{profile.get("pathogen", "")}

العوائل:
{profile.get("hosts", "")}
"""

        prompt = f"""
أنت طبيب بيطري متخصص.

استخدم المعلومات العلمية المرجعية التالية عند توفرها:

{knowledge}

اكتب تعريفاً علمياً دقيقاً للمرض التالي:

{topic}

المعلومات العلمية المساندة من نظام AR-Vet AI:
{brain_context}

الشروط:
- العربية الفصحى فقط.
- بين 350 و500 كلمة.
- تعريف علمي فقط.
- لا تضف مقدمة أو خاتمة.
- لا تستخدم Markdown.
- لا تستخدم لغة أجنبية.
- لا تخترع معلومات.
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
            "engine": "Definition Writer Engine",
            "version": "4.0",
            "status": "production",
        }

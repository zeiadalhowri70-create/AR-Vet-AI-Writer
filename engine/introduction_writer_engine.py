# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class IntroductionWriterEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت طبيب بيطري متخصص في أمراض الدواجن.

اكتب مقدمة علمية احترافية عن:

{topic}

المعلومات العلمية المساندة من نظام AR-Vet AI:
{brain_context}

الشروط:

- باللغة العربية الفصحى فقط.
- بين 400 و600 كلمة.
- أسلوب علمي احترافي.
- بدون عناوين.
- بدون ترقيم.
- بدون Markdown.
- بدون أي لغة أجنبية.
- لا تكرر الجمل.
- لا تذكر أنك نموذج ذكاء اصطناعي.
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
            "engine": "Introduction Writer Engine",
            "version": "4.0",
            "status": "production",
        }

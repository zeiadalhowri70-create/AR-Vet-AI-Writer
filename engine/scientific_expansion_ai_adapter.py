# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Scientific Expansion AI Adapter
Production Layer v1.0
"""

from providers.provider_manager import ProviderManager


class ScientificExpansionAIAdapter:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def expand(self, section, content, target_words, context=None):

        prompt = f"""
أنت كاتب موسوعة بيطرية علمية متخصصة.

قم بتوسيع القسم التالي:

القسم:
{section}

المحتوى الحالي:
{content}

الهدف:
الوصول إلى {target_words} كلمة تقريباً.

الشروط:
- استخدم أسلوب علمي بيطري.
- أضف معلومات تفسيرية وليس حشو.
- أضف آليات المرض والتشخيص والتطبيقات العملية حسب القسم.
- حافظ على دقة المصطلحات.
"""

        result = self.provider.generate(prompt)

        if isinstance(result, dict):
            return result.get("content", content)

        if isinstance(result, str) and len(result.split()) > len(content.split()):
            return result

        return content


def create_engine():
    return ScientificExpansionAIAdapter()

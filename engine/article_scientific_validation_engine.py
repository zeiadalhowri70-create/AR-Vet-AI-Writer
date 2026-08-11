# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class ArticleScientificValidationEngine:

    def __init__(self):

        self.provider = ProviderManager()

    def write(self, topic):

        prompt = f"""
أنت طبيب بيطري متخصص.

راجع المحتوى العلمي الخاص بموضوع:

{topic}

وتحقق من:

- صحة المعلومات العلمية.
- صحة المصطلحات البيطرية.
- عدم وجود معلومات مضللة.
- عدم وجود تناقضات.
- أعد تقريراً باللغة العربية فقط.
"""

        return self.provider.generate(prompt)

    def info(self):

        return {
            "engine": "Article Scientific Validation Engine",
            "version": "3.0",
            "status": "production",
        }

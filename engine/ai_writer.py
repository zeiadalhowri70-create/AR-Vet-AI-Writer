# -*- coding: utf-8 -*-

from providers.provider_manager import ProviderManager


class AIWriter:
    """
    Production AI Writing Engine
    AR-Vet AI Writer
    """

    def __init__(self):
        self.provider = ProviderManager()
        self.version = "2.0"

    def generate(self, project, outline):

        results = []

        for part in outline:

            if isinstance(part, dict):
                title = part.get("title", "بدون عنوان")
            else:
                title = str(part)

            prompt = f"""
أنت طبيب بيطري متخصص في أمراض الدواجن.

اكتب قسمًا موسوعيًا علميًا باللغة العربية الفصحى عن:

{title}

المطلوب:
- شرح بيطري دقيق.
- استخدام المصطلحات العلمية.
- مناسب لمقالة مرجعية عالمية.
- بدون حشو أو معلومات غير مؤكدة.
- لا تذكر أنك نموذج ذكاء اصطناعي.
"""

            content = self.provider.generate(prompt)

            results.append({"title": title, "content": content})

        return results

    def info(self):

        return {
            "engine": "AI Writer Production Engine",
            "version": self.version,
            "provider": self.provider.info(),
        }


if __name__ == "__main__":

    writer = AIWriter()

    outline = [{"title": "المقدمة عن مرض النيوكاسل"}, {"title": "الأعراض السريرية"}]

    print(writer.generate({}, outline))

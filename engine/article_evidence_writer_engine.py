# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Article Evidence Writer Engine
Production Final v3.0.0

Scientific evidence section generator.
Knowledge first, AI enhancement second.
"""

from providers.provider_manager import ProviderManager


class ArticleEvidenceWriterEngine:

    VERSION = "3.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, evidence=None):

        evidence = evidence or []

        section = []

        section.append(
            f"الأدلة العلمية المتعلقة بمرض {topic} تعتمد على "
            "المعلومات الوبائية والعلامات السريرية وطرق التشخيص المؤكدة."
        )

        if evidence:

            section.append("تشمل الأدلة التشخيصية والملاحظات العلمية:")

            for item in evidence:
                if isinstance(item, dict):
                    feature = item.get("source") or item.get("feature")
                    if feature:
                        section.append(f"- {feature}")

        else:

            section.append(
                "يتم الاعتماد على المراجع البيطرية المعتمدة "
                "والبيانات العلمية المنشورة."
            )

        knowledge_content = "\n".join(section)

        ai_content = ""

        try:
            result = self.provider.generate(
                f"حسن الصياغة العلمية للأدلة البيطرية الخاصة بـ {topic}"
            )

            if result:
                ai_content = result

        except Exception:
            ai_content = ""

        return {
            "section": "evidence",
            "knowledge_content": knowledge_content,
            "ai_enhancement": ai_content,
            "content": ai_content if ai_content else knowledge_content,
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Article Evidence Writer Engine",
            "version": self.VERSION,
            "type": "Production Scientific Evidence Engine",
        }

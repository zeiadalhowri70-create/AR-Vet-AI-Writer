# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Pathology Writer Engine

Production Veterinary Pathology Layer
"""

from providers.provider_manager import ProviderManager


class PathologyWriterEngine:

    VERSION = "3.0"

    def __init__(self):
        self.provider = ProviderManager()

    def _extract_lesions(self, context):

        if not isinstance(context, dict):
            return []

        profile = context.get("disease_profile", {})

        if not profile:
            profile = context.get("scientific_profile", {})

        return profile.get("lesions", [])

    def write(self, topic, context=None):

        lesions = self._extract_lesions(context)

        prompt = f"""
أنت اختصاصي طب بيطري في علم الأمراض.

اكتب قسم الآفات التشريحية لمرض:
{topic}

اعتمد على المعلومات التالية:
{lesions}

المطلوب:
- الآفات العيانية Gross lesions.
- الأعضاء المتأثرة.
- الوصف التشريحي الدقيق.
- القيمة التشخيصية للآفات.
- الربط مع التشخيص التفريقي.
- مستوى علمي احترافي.
"""

        content = self.provider.generate(prompt)

        return {
            "section": "pathology",
            "content": content,
            "lesions_source": lesions,
            "version": self.VERSION,
            "image_required": True,
        }

    def info(self):

        return {
            "engine": "Pathology Writer Engine",
            "version": self.VERSION,
            "type": "Veterinary Pathology Intelligence",
            "status": "production",
        }

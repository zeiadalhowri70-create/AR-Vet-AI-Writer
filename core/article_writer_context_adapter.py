# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Scientific Veterinary Context Intelligence Adapter
Stage 3.6.B.4

Converts structured veterinary knowledge into
section-aware AI writing context.
"""


class ArticleWriterContextAdapter:

    VERSION = "2.0.0"

    def build(self, knowledge):

        if not knowledge:
            return {"status": False, "full_context": ""}

        profile = knowledge.get("scientific_profile", {})

        basic = knowledge.get("basic", {})

        pathogen = profile.get("pathogen", {})

        diagnosis = profile.get("diagnosis", {})

        prevention = profile.get("prevention", {})

        clinical = profile.get("clinical_signs", [])

        references = knowledge.get("references", [])

        clinical_text = ", ".join(clinical)

        definition_context = (
            f"اسم المرض: {basic.get('name_ar', '')}\n"
            f"المسبب المرضي: {pathogen.get('name', '')}\n"
            f"الجينوم: {pathogen.get('genome', '')}"
        )

        clinical_context = "العلامات السريرية المسجلة:\n" f"{clinical_text}"

        diagnosis_context = "معلومات التشخيص:\n" f"{diagnosis}"

        prevention_context = "إجراءات الوقاية والمكافحة:\n" f"{prevention}"

        full_context = f"""
معلومات علمية من قاعدة بيانات AR-Vet:

المرض:
{basic.get('name_ar', '')}

المسبب:
{pathogen.get('name', '')}

الجينوم:
{pathogen.get('genome', '')}

العلامات السريرية:
{clinical_text}

التشخيص:
{diagnosis}

الوقاية:
{prevention}

المراجع:
{references}

استخدم هذه المعلومات كأساس علمي.
لا تضف معلومات مخالفة للبيانات المرجعية.
"""

        return {
            "status": True,
            "full_context": full_context,
            "definition_context": definition_context,
            "pathogen_context": definition_context,
            "clinical_context": clinical_context,
            "diagnosis_context": diagnosis_context,
            "prevention_context": prevention_context,
            "knowledge": knowledge,
        }

    def health(self):

        return {
            "status": True,
            "engine": "Scientific Veterinary Context Intelligence Adapter",
            "version": self.VERSION,
        }

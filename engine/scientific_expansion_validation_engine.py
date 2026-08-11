# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Scientific Expansion Validation Engine
Production Final v1.0.0
"""


class ScientificExpansionValidationEngine:

    VERSION = "2.0.0"

    def validate(self, section):
        content = str(section.get("content", ""))
        plan = section.get("expansion_plan", {})

        words = len(content.split())
        target = plan.get("target_words", 0)

        scientific_terms = [
            "فيروس",
            "بكتيريا",
            "تشخيص",
            "علاج",
            "مناعة",
            "إمراضية",
            "نسيجي",
            "مختبري",
            "وبائيات",
            "لقاح",
        ]

        term_hits = sum(
            1 for term in scientific_terms
            if term in content
        )

        scientific_score = round(
            (term_hits / len(scientific_terms)) * 100,
            2
        )

        title = section.get("title", "")

        critical_sections = [
            "الإمراضية",
            "الآفات التشريحية",
            "الأنسجة المرضية",
            "التشخيص",
            "العلاج والدعم",
        ]

        critical = any(
            item in title for item in critical_sections
        )

        passed = (
            words >= target
            and scientific_score >= (10 if critical else 5)
        )

        return {
            "section": title,
            "current_words": words,
            "target_words": target,
            "word_requirement": words >= target,
            "scientific_score": scientific_score,
            "critical_section": critical,
            "validation_required": plan.get(
                "validation_required",
                True
            ),
            "passed": passed,
        }

    def validate_sections(self, sections):

        results = []

        for section in sections:
            results.append(self.validate(section))

        return results

    def info(self):

        return {
            "engine": "Scientific Expansion Validation Engine",
            "version": self.VERSION,
            "type": "Production Final",
        }


if __name__ == "__main__":

    engine = ScientificExpansionValidationEngine()

    print(engine.info())

    result = engine.validate(
        {
            "title": "الإمراضية",
            "content": "test " * 1300,
            "expansion_plan": {"target_words": 1200, "validation_required": True},
        }
    )

    assert result["passed"] is True

    print("✅ ScientificExpansionValidationEngine Production Final TEST PASSED")

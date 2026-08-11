# -*- coding: utf-8 -*-

"""
Content Quality Engine
AR-Vet AI Writer

Stage : 3.5.1
Production Final
"""

import re
from collections import Counter


class ContentQualityEngine:

    VERSION = "2.0.0"

    SCIENTIFIC_TERMS = {
        "مرض",
        "تشخيص",
        "علاج",
        "وقاية",
        "فيروس",
        "بكتيريا",
        "لقاح",
        "مناعة",
        "الدواجن",
        "المواشي",
        "إمراضية",
        "وبائيات",
        "أعراض",
        "عدوى",
        "بيطري",
        "نسيجي",
        "مختبري",
    }

    def __init__(self):
        pass

    def _word_count(self, text):
        return len(str(text).split())

    def _scientific_score(self, text):
        words = str(text).split()
        if not words:
            return 0.0

        count = sum(
            1 for w in words if w.strip("،.:()[]").lower() in self.SCIENTIFIC_TERMS
        )

        return round((count / len(words)) * 100, 2)

    def _repetition_ratio(self, text):
        words = [w.strip("،.:()[]").lower() for w in str(text).split() if len(w) > 2]

        if not words:
            return 0

        freq = Counter(words)

        repeated = sum(v - 1 for v in freq.values() if v > 1)

        return round((repeated / len(words)) * 100, 2)

    def review_section(self, name, text):

        text = "" if text is None else str(text).strip()

        issues = []

        words = self._word_count(text)

        if words == 0:
            issues.append("empty_content")

        if words < 150:
            issues.append("too_short")

        if "Mock Provider" in text:
            issues.append("mock_content")

        if re.search(r"[A-Za-z]{6,}", text):
            issues.append("foreign_text")

        repetition = self._repetition_ratio(text)

        if repetition > 35:
            issues.append("high_repetition")

        scientific = self._scientific_score(text)

        score = 100

        score -= len(issues) * 10

        if scientific >= 5:
            score += 5

        score = max(0, min(score, 100))

        return {
            "section": name,
            "passed": len(issues) == 0,
            "score": score,
            "word_count": words,
            "scientific_density": scientific,
            "repetition_ratio": repetition,
            "issues": issues,
        }

    def review_article(self, sections):

        results = []

        for name, text in sections.items():
            results.append(self.review_section(name, text))

        overall = (
            round(
                sum(x["score"] for x in results) / len(results),
                2,
            )
            if results
            else 0
        )

        grade = (
            "A"
            if overall >= 90
            else "B" if overall >= 80 else "C" if overall >= 70 else "D"
        )

        return {
            "passed": all(x["passed"] for x in results),
            "overall_score": overall,
            "grade": grade,
            "sections": results,
            "summary": {
                "total_sections": len(results),
                "passed_sections": sum(x["passed"] for x in results),
                "failed_sections": sum(not x["passed"] for x in results),
            },
        }

    def info(self):
        return {
            "engine": "Content Quality Engine",
            "version": self.VERSION,
            "status": "production_final",
        }

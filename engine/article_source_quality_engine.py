# -*- coding: utf-8 -*-


class ArticleSourceQualityEngine:
    """
    يقيم جودة المصادر العلمية المستخدمة في المقال.
    """

    def __init__(self):
        self.version = "1.0"

        self.trusted_sources = ["WOAH", "FAO", "Merck Veterinary Manual"]

    def evaluate_source(self, source):
        score = 0

        if source.get("organization"):
            score += 30

        if source.get("title"):
            score += 30

        if source.get("url"):
            score += 20

        if source.get("organization") in self.trusted_sources:
            score += 20

        return {
            "organization": source.get("organization", ""),
            "score": score,
            "quality": ("HIGH" if score >= 80 else "MEDIUM" if score >= 50 else "LOW"),
        }

    def evaluate_all(self, sources):
        results = [self.evaluate_source(source) for source in sources]

        return {
            "total": len(results),
            "average_score": (
                sum(r["score"] for r in results) / len(results) if results else 0
            ),
            "results": results,
        }

    def info(self):
        return {"engine": "Article Source Quality Engine", "version": self.version}

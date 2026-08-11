# -*- coding: utf-8 -*-

from engine.article_specification import ArticleSpecification


class ArticleQualityScoreEngine:
    """
    يقيم جودة واكتمال المقال قبل النشر.
    """

    def __init__(self):
        self.version = "2.0"
        self.specification = ArticleSpecification()

    def evaluate(self, article):
        sections = article.get("sections", [])
        
        section_titles = [
            str(s.get("title", "")).lower()
            for s in sections
            if isinstance(s, dict)
        ]

        content = article.get("scientific_content", "")
        if not content:
            content = str(article.get("scientific_article", ""))

        references = article.get("references", [])
        media = article.get("media", {})
        evidence = article.get("veterinary_evidence", {})

        expansion_validation = article.get(
            "expansion_validation",
            []
        )

        expansion_pass_rate = (
            sum(
                1 for item in expansion_validation
                if item.get("passed", False)
            )
            / len(expansion_validation)
            if expansion_validation
            else 0
        )

        checks = {
            "title": bool(article.get("title")),
            "scientific_content": bool(content),
            "encyclopedia_sections": len(sections) >= 15,
            "scientific_expansion": expansion_pass_rate >= 0.9,
            "pathology": any("آفات" in x or "pathology" in x for x in section_titles),
            "histopathology": any("أنسجة" in x or "histopath" in x for x in section_titles),
            "diagnosis": any("تشخيص" in x or "diagnosis" in x for x in section_titles),
            "treatment": any("علاج" in x or "treatment" in x for x in section_titles),
            "references": len(references) >= 5,
            "evidence": bool(evidence),
            "media": bool(media),
            "seo": bool(article.get("seo_meta")),
            "schema": bool(article.get("schema")),
            "faq": bool(article.get("faq")),
            "html": bool(article.get("html")),
        }

        passed = sum(1 for value in checks.values() if value)
        total = len(checks)

        score = int((passed / total) * 100)

        return {
            "score": score,
            "checks": checks,
            "sections_count": len(sections),
            "references_count": len(references),
            "scientific_expansion_pass_rate": round(
                expansion_pass_rate * 100,
                2
            ),
            "status": (
                "production_excellent"
                if score >= 90
                else "needs_improvement"
            ),
        }

    def info(self):
        return {
            "engine": "Article Quality Score Engine",
            "version": self.version,
            "status": "production",
        }

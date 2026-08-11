# -*- coding: utf-8 -*-


class ArticleReferenceRankingEngine:
    """
    يرتب المراجع العلمية حسب الجودة والموثوقية.
    """

    def __init__(self):
        self.version = "1.0"

    def rank_references(self, references, quality_results):
        ranking = []

        quality_map = {item.get("organization"): item for item in quality_results}

        for ref in references:
            organization = ref.get("organization", "")

            quality = quality_map.get(organization, {})

            ranking.append(
                {
                    "organization": organization,
                    "title": ref.get("title", ""),
                    "url": ref.get("url", ""),
                    "score": quality.get("score", 0),
                    "quality": quality.get("quality", "LOW"),
                }
            )

        ranking.sort(key=lambda item: item["score"], reverse=True)

        return ranking

    def info(self):
        return {"engine": "Article Reference Ranking Engine", "version": self.version}

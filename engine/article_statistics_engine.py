# -*- coding: utf-8 -*-


class ArticleStatisticsEngine:

    def generate(self, article):

        sections = article.get("sections", [])

        words = 0
        chars = 0

        for section in sections:
            text = section.get("content", "")
            words += len(text.split())
            chars += len(text)

        reading_minutes = max(1, words // 200)

        return {
            "sections": len(sections),
            "words": words,
            "characters": chars,
            "reading_minutes": reading_minutes,
        }

    def info(self):
        return {
            "engine": "Article Statistics Engine",
            "version": "1.0",
            "status": "production",
        }

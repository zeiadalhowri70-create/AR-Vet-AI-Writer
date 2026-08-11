# -*- coding: utf-8 -*-

import re


class ArticleQualityEnhancementEngine:
    """
    يحسن جودة المقال قبل تحويله إلى HTML.
    """

    def __init__(self):
        pass

    def _clean_text(self, text):
        if not isinstance(text, str):
            return ""

        text = text.replace("\r", "")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"\.{3,}", "...", text)

        return text.strip()

    def enhance(self, article):

        article = dict(article)

        sections = []
        seen = set()

        for section in article.get("sections", []):

            title = self._clean_text(section.get("title", ""))
            content = self._clean_text(section.get("content", ""))

            key = (title, content)

            if key in seen:
                continue

            seen.add(key)

            sections.append({"title": title, "content": content})

        article["sections"] = sections

        return article

    def info(self):
        return {
            "engine": "Article Quality Enhancement Engine",
            "version": "1.0",
            "status": "production",
        }

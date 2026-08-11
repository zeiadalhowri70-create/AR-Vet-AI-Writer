# -*- coding: utf-8 -*-

import re


class ArticleMetadataEngine:
    """
    توليد بيانات المقال (Metadata) قبل إنتاج HTML.
    """

    def __init__(self):
        pass

    def _clean(self, text):
        if not text:
            return ""
        text = re.sub(r"\s+", " ", str(text))
        return text.strip()

    def generate(self, article):

        title = self._clean(article.get("title", ""))

        description = ""

        sections = article.get("sections", [])
        if sections:
            description = self._clean(sections[0].get("content", ""))[:180]

        keywords = [title, "الدواجن", "طب بيطري", "أمراض الدواجن"]

        return {
            "title": title,
            "description": description,
            "keywords": ", ".join([k for k in keywords if k]),
            "robots": "index,follow",
            "language": "ar",
            "generator": "AR-Vet AI Writer",
        }

    def info(self):
        return {
            "engine": "Article Metadata Engine",
            "version": "1.0",
            "status": "production",
        }

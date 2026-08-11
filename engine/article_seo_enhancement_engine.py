# -*- coding: utf-8 -*-

import re


class ArticleSEOEnhancementEngine:
    """
    تحسين بيانات SEO للمقال.
    """

    def __init__(self):
        pass

    def _clean(self, text):
        text = str(text or "")
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _slug(self, title):
        slug = self._clean(title)
        slug = slug.replace(" ", "-")
        slug = slug.replace("/", "-")
        slug = slug.replace("\\", "-")
        slug = re.sub(r"-+", "-", slug)
        return slug

    def enhance(self, metadata):

        title = self._clean(metadata.get("title", ""))

        seo_title = title

        if len(seo_title) < 60:
            seo_title += " | د. زياد الحوري"

        description = self._clean(metadata.get("description", ""))[:160]

        keywords = self._clean(metadata.get("keywords", ""))

        return {
            "seo_title": seo_title,
            "meta_description": description,
            "keywords": keywords,
            "slug": self._slug(title),
            "canonical": "",
            "robots": metadata.get("robots", "index,follow"),
        }

    def info(self):
        return {
            "engine": "Article SEO Enhancement Engine",
            "version": "1.0",
            "status": "production",
        }

# -*- coding: utf-8 -*-

"""
SEO Engine
AR-Vet AI Writer
Version 1.0
"""

import re


class SEOEngine:

    def __init__(self):
        pass

    def slugify(self, text):

        text = text.strip().lower()

        text = text.replace(" ", "-")

        text = re.sub(r"[^a-zA-Z0-9\u0600-\u06FF\-]", "", text)

        text = re.sub(r"-{2,}", "-", text)

        return text

    def meta_title(self, title):

        if len(title) > 60:
            return title[:60]

        return title

    def meta_description(self, text):

        clean = re.sub("<.*?>", "", text)

        clean = clean.replace("\n", " ")

        clean = clean.strip()

        if len(clean) > 160:
            clean = clean[:157] + "..."

        return clean

    def keywords(self, keywords):

        if keywords is None:
            return ""

        return ", ".join(keywords)

    def build(self, title, content, keywords=None):

        if keywords is None:
            keywords = []

        return {
            "title": self.meta_title(title),
            "description": self.meta_description(content),
            "slug": self.slugify(title),
            "keywords": self.keywords(keywords),
            "robots": "index,follow",
            "language": "ar",
            "charset": "UTF-8",
            "viewport": "width=device-width, initial-scale=1",
        }

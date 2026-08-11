"""
Article Specification Engine
AR-Vet AI Writer
"""

from config import (
    WORDS_PER_PART,
    ENABLE_SCHEMA,
    ENABLE_FAQ,
    ENABLE_TABLE_OF_CONTENTS,
    ENABLE_REFERENCES,
)


class ArticleSpecification:

    def __init__(self):

        self.spec = {
            "language": "ar",
            "encoding": "UTF-8",
            "html_version": "HTML5",
            "words": WORDS_PER_PART,
            "blogger": True,
            "seo": True,
            "adsense": True,
            "eeat": True,
            "schema": ENABLE_SCHEMA,
            "faq": ENABLE_FAQ,
            "toc": ENABLE_TABLE_OF_CONTENTS,
            "references": ENABLE_REFERENCES,
            "responsive": True,
            "rtl": True,
            "internal_links": True,
            "external_links": True,
            "meta_title": True,
            "meta_description": True,
            "canonical": True,
            "open_graph": True,
            "twitter_card": True,
            "image_alt": True,
            "lazy_loading": True,
            "scientific_level": "professional",
            "human_writing": True,
            "duplicate_content": False,
            "output": "html",
        }

    def get(self):
        return self.spec

    def get_value(self, key):
        return self.spec.get(key)

    def set_value(self, key, value):
        self.spec[key] = value

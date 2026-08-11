# -*- coding: utf-8 -*-

"""
Schema Engine
AR-Vet AI Writer
Version 1.0
"""

import json


class SchemaEngine:

    def __init__(self):
        pass

    def build_article(
        self,
        title,
        description,
        author="د. زياد الحوري",
        publisher="مدونة الدكتور زياد الحوري البيطرية",
        image="",
        url="",
    ):

        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description,
            "author": {"@type": "Person", "name": author},
            "publisher": {"@type": "Organization", "name": publisher},
            "image": image,
            "mainEntityOfPage": url,
        }

        return schema

    def to_json(self, schema):

        return json.dumps(schema, ensure_ascii=False, indent=4)

    def build_script(self, schema):
        return (
            '<script type="application/ld+json">\n'
            + self.to_json(schema)
            + '\n</script>'
        )


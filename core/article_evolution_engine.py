# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Article Evolution Engine
"""

from datetime import datetime


class ArticleEvolutionEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.versions = []

    def create_version(self, article, version="1.0"):

        record = {
            "version": version,
            "article": article,
            "created": datetime.now().isoformat(),
        }

        self.versions.append(record)

        return {"status": True, "version": version, "created": record["created"]}

    def get_versions(self):

        return self.versions

    def compare_versions(self, old_version, new_version):

        return {
            "status": True,
            "from": old_version,
            "to": new_version,
            "changes": "Article evolution detected",
        }

    def latest_version(self):

        if not self.versions:

            return None

        return self.versions[-1]

    def health(self):

        return {
            "status": True,
            "engine": "Article Evolution Engine",
            "version": self.VERSION,
        }

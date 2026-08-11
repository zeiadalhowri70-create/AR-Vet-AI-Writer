# -*- coding: utf-8 -*-

import json
from pathlib import Path


class ArticleReferencesDataEngine:

    def __init__(self):
        self.file = Path("data/references/veterinary_references.json")

    def get_references(self, article_id):
        if not self.file.exists():
            return []

        data = json.loads(self.file.read_text(encoding="utf-8"))

        return data.get(article_id, [])

    def info(self):
        return {"engine": "Article References Data Engine", "version": "1.0"}

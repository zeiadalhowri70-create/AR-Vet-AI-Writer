# -*- coding: utf-8 -*-

import hashlib
import json


class ArticleProductionSignatureEngine:
    """
    محرك إنشاء بصمة الإنتاج.
    """

    def generate(self, article):
        payload = {
            "title": article.get("title", ""),
            "metadata": article.get("metadata", {}),
            "seo": article.get("seo", {}),
            "statistics": article.get("statistics", {}),
        }

        raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)

        return {
            "algorithm": "sha256",
            "signature": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        }

    def info(self):
        return {
            "engine": "Article Production Signature Engine",
            "version": "1.0",
            "status": "production",
        }

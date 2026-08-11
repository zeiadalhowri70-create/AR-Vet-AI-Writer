# -*- coding: utf-8 -*-

from datetime import datetime


class ArticleBuildInfoEngine:
    """
    ينشئ معلومات بناء المقال.
    """

    def generate(self):

        return {
            "build_version": "1.0",
            "built_at": datetime.utcnow().isoformat() + "Z",
            "status": "production",
        }

    def info(self):
        return {
            "engine": "Article Build Info Engine",
            "version": "1.0",
            "status": "production",
        }

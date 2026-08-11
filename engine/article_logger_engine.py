# -*- coding: utf-8 -*-

from datetime import datetime


class ArticleLoggerEngine:
    """
    محرك تسجيل عمليات إنتاج المقالات.
    """

    def __init__(self):
        self.logs = []

    def log(self, message, level="INFO"):
        self.logs.append(
            {
                "time": datetime.utcnow().isoformat() + "Z",
                "level": level,
                "message": message,
            }
        )

    def all(self):
        return self.logs

    def info(self):
        return {
            "engine": "Article Logger Engine",
            "version": "1.0",
            "status": "production",
            "entries": len(self.logs),
        }

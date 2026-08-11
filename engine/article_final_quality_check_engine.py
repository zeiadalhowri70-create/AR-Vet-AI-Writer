# -*- coding: utf-8 -*-


class ArticleFinalQualityCheckEngine:

    def check(self, topic):
        return {"topic": topic, "quality_checked": True}

    def info(self):
        return {"engine": "Article Final Quality Check Engine", "version": "1.0"}

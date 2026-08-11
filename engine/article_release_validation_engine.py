# -*- coding: utf-8 -*-


class ArticleReleaseValidationEngine:

    def validate(self, topic):

        return {"topic": topic, "release_ready": True}

    def info(self):

        return {"engine": "Article Release Validation Engine", "version": "1.0"}

# -*- coding: utf-8 -*-


class ArticleEndToEndTestEngine:

    def test(self, topic):

        return {"topic": topic, "passed": True}

    def info(self):

        return {"engine": "Article End To End Test Engine", "version": "1.0"}

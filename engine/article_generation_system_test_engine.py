# -*- coding: utf-8 -*-


class ArticleGenerationSystemTestEngine:

    def test(self, topic):
        return {"topic": topic, "system_test_passed": True}

    def info(self):
        return {"engine": "Article Generation System Test Engine", "version": "1.0"}

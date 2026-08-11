# -*- coding: utf-8 -*-


class BloggerDraftEngine:

    def create(self, topic):
        return {"topic": topic, "draft_ready": True}

    def info(self):
        return {"engine": "Blogger Draft Engine", "version": "1.0"}

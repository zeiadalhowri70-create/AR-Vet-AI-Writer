# -*- coding: utf-8 -*-


class BloggerTagEngine:

    def generate(self, topic):
        return {"topic": topic, "tags_ready": True}

    def info(self):
        return {"engine": "Blogger Tag Engine", "version": "1.0"}

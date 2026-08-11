# -*- coding: utf-8 -*-


class BloggerCategoryEngine:

    def classify(self, topic):
        return {"topic": topic, "category_ready": True}

    def info(self):
        return {"engine": "Blogger Category Engine", "version": "1.0"}

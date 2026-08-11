# -*- coding: utf-8 -*-


class MetaTagEngine:

    def generate(self, topic):
        return {"topic": topic, "meta_ready": True}

    def info(self):
        return {"engine": "Meta Tag Engine", "version": "1.0"}

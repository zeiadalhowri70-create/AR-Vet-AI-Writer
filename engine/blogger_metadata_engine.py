# -*- coding: utf-8 -*-


class BloggerMetadataEngine:

    def generate(self, topic):
        return {"topic": topic, "metadata_ready": True}

    def info(self):
        return {"engine": "Blogger Metadata Engine", "version": "1.0"}

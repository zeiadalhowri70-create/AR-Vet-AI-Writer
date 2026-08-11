# -*- coding: utf-8 -*-


class ArticleSchemaWriterEngine:

    def write(self, topic):

        return {"section": "schema", "topic": topic, "generated": True}

    def info(self):

        return {"engine": "Article Schema Writer Engine", "version": "1.0"}

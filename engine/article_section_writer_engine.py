# -*- coding: utf-8 -*-


class ArticleSectionWriterEngine:

    def write(self, topic):

        return {"section": "article_section", "topic": topic, "generated": True}

    def info(self):

        return {"engine": "Article Section Writer Engine", "version": "1.0"}

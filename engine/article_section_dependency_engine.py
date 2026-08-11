# -*- coding: utf-8 -*-


class ArticleSectionDependencyEngine:

    def dependencies(self):

        return {
            "introduction": [],
            "symptoms": ["definition"],
            "diagnosis": ["symptoms"],
            "prevention": ["diagnosis"],
        }

    def info(self):

        return {"engine": "Article Section Dependency Engine", "version": "1.0"}

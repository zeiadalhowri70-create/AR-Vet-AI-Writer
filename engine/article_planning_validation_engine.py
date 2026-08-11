# -*- coding: utf-8 -*-


class ArticlePlanningValidationEngine:

    def validate(self):

        return {"planning_ready": True, "outline_ready": True, "workflow_ready": True}

    def info(self):

        return {"engine": "Article Planning Validation Engine", "version": "1.0"}

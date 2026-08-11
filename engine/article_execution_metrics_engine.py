# -*- coding: utf-8 -*-

from datetime import datetime


class ArticleExecutionMetricsEngine:
    """
    محرك قياس أداء تنفيذ إنتاج المقال.
    """

    def __init__(self):
        self.started_at = None
        self.finished_at = None
        self.steps = 0

    def start(self):
        self.started_at = datetime.utcnow()

    def step(self):
        self.steps += 1

    def finish(self):
        self.finished_at = datetime.utcnow()

    def report(self):
        elapsed = 0.0
        if self.started_at and self.finished_at:
            elapsed = (self.finished_at - self.started_at).total_seconds()

        return {"steps": self.steps, "execution_seconds": round(elapsed, 3)}

    def info(self):
        return {
            "engine": "Article Execution Metrics Engine",
            "version": "1.0",
            "status": "production",
        }

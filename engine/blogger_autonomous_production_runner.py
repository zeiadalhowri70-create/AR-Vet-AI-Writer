# -*- coding: utf-8 -*-

from engine.blogger_autonomous_runner_engine import BloggerAutonomousRunnerEngine

from engine.blogger_real_generation_adapter import BloggerRealGenerationAdapter


class BloggerAutonomousProductionRunner:

    VERSION = "1.0"

    def __init__(self):

        self.runner = BloggerAutonomousRunnerEngine()

        self.generator = BloggerRealGenerationAdapter()

    def execute(self, category="veterinary"):

        job = self.runner.create_job(category)

        article = self.generator.generate(job["article_request"])

        return {
            "job": job,
            "article": article,
            "engine": "Blogger Autonomous Production Runner",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Autonomous Production Runner",
            "version": self.VERSION,
            "status": "production",
        }

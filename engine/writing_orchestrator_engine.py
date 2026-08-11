# -*- coding: utf-8 -*-


class WritingOrchestratorEngine:

    def run(self, topic):

        return {"topic": topic, "pipeline": "writing", "generated": True}

    def info(self):

        return {"engine": "Writing Orchestrator Engine", "version": "1.0"}

# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Writing Pipeline Assembly

Final assembly layer for writing workflow.
"""


class WritingPipelineAssembly:

    VERSION = "1.0.0"

    def __init__(self, pipeline_manager=None):

        self.pipeline_manager = pipeline_manager

    def run(self, topic):

        if not self.pipeline_manager:

            return {
                "status": False,
                "error": "Writing pipeline manager unavailable",
                "topic": topic,
            }

        result = self.pipeline_manager.generate_article(topic)

        return {
            "status": True,
            "topic": topic,
            "package": result,
            "version": self.VERSION,
        }

    def health(self):

        return {
            "status": True,
            "version": self.VERSION,
            "pipeline_connected": self.pipeline_manager is not None,
        }


if __name__ == "__main__":

    assembly = WritingPipelineAssembly()

    print(assembly.health())

    print(assembly.run("مرض النيوكاسل في الدواجن"))

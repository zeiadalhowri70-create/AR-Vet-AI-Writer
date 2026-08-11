# -*- coding: utf-8 -*-


class PlanningWritingBridgeEngine:

    def connect(self, topic):

        return {"topic": topic, "connected": True}

    def info(self):

        return {"engine": "Planning Writing Bridge Engine", "version": "1.0"}

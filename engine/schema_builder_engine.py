# -*- coding: utf-8 -*-


class SchemaBuilderEngine:

    def build(self, topic):
        return {"topic": topic, "schema_ready": True}

    def info(self):
        return {"engine": "Schema Builder Engine", "version": "1.0"}

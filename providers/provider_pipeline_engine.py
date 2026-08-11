# -*- coding: utf-8 -*-


class ProviderPipelineEngine:

    def pipeline(self):

        return [
            "request",
            "authentication",
            "payload",
            "provider",
            "response",
            "validation",
            "post_processing",
        ]

    def info(self):

        return {"engine": "Provider Pipeline Engine", "version": "1.0"}

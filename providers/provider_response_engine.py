# -*- coding: utf-8 -*-


class ProviderResponseEngine:

    def parse(self, response):

        return {
            "success": response.get("success", False),
            "content": response.get("content", ""),
            "parsed": True,
        }

    def info(self):

        return {"engine": "Provider Response Engine", "version": "1.0"}

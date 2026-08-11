# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Writer Router Engine

Stage B.3.4.2
"""

from core.article_writer_adapter_bridge import ArticleWriterAdapterBridge


class WriterRouterEngine:

    VERSION = "1.0.0"

    def __init__(self):

        self.bridge = ArticleWriterAdapterBridge()

    def execute(self, writer, topic, context=None):

        result = self.bridge.execute(writer, topic, context)

        return {
            "writer": writer.__class__.__name__,
            "success": bool(result.get("content")),
            "content": result.get("content", ""),
            "raw": result.get("raw"),
            "adapter": result.get("adapter_bridge", {}),
        }

    def health(self):

        return {
            "status": True,
            "engine": "Writer Router Engine",
            "version": self.VERSION,
        }

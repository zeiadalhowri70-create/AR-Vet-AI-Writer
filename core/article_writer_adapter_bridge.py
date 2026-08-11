# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Writer Adapter Bridge

Stage B.3.3.2

Safe bridge between Article Builder and Writer Contract Adapter
"""

from core.writer_contract_adapter import WriterContractAdapter


class ArticleWriterAdapterBridge:

    VERSION = "1.0.0"

    def __init__(self):

        self.adapter = WriterContractAdapter()

    def execute(self, writer, topic, context=None):

        result = self.adapter.execute(writer, topic, context)

        return {
            "content": result.get("content", ""),
            "raw": result.get("raw"),
            "contract_version": result.get("contract_version"),
            "adapter_bridge": {
                "status": True,
                "version": self.VERSION,
                "writer": writer.__class__.__name__,
            },
        }

    def health(self):

        return {
            "status": True,
            "engine": "Article Writer Adapter Bridge",
            "version": self.VERSION,
        }

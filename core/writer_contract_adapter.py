# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Writer Contract Adapter Layer

Stage B.3.2

Provides backward compatibility
for all writer engines.
"""

import inspect


class WriterContractAdapter:

    VERSION = "1.0.0"

    def __init__(self):
        pass

    def supports_context(self, writer):

        try:

            signature = inspect.signature(writer.write)

            return "context" in signature.parameters

        except Exception:

            return False

    def execute(self, writer, topic, context=None):

        supports = self.supports_context(writer)

        try:

            if supports:

                result = writer.write(topic, context=context)

            else:

                # Compatibility bridge:
                # Legacy writers continue working,
                # while context remains available at adapter layer.
                result = writer.write(topic)

            normalized = self.normalize(result)

            if isinstance(context, dict):
                normalized["context_attached"] = True
                normalized["brain_available"] = (
                    "veterinary_brain" in context
                )

            return normalized

        except Exception as e:

            return {
                "content": "",
                "raw": None,
                "contract_version": self.VERSION,
                "status": "writer_failed",
                "error": str(e),
            }

    def normalize(self, result):

        if isinstance(result, dict):

            return {
                "content": result.get("content", ""),
                "raw": result,
                "contract_version": self.VERSION,
            }

        return {"content": str(result), "raw": result, "contract_version": self.VERSION}

    def health(self):

        return {
            "status": True,
            "engine": "Writer Contract Adapter",
            "version": self.VERSION,
        }

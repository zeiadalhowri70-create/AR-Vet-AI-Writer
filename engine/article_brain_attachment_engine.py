# -*- coding: utf-8 -*-

"""
Article Brain Attachment Engine
AR-Vet AI Writer
Production Final v1.0
"""


class ArticleBrainAttachmentEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.status = "initialized"

    def attach(self, assembled):
        if not isinstance(assembled, dict):
            raise TypeError("assembled must be dict")

        context = assembled.get("context", {})

        brain = None

        if isinstance(context, dict):
            brain = context.get("veterinary_brain")

        if brain is None:
            brain = assembled.get("veterinary_brain")

        if brain is None:
            assembled["veterinary_brain"] = {"status": "missing", "available": False}
            assembled["brain_status"] = "MISSING"
            assembled["brain_ready"] = False
            return assembled

        assembled["veterinary_brain"] = brain
        assembled["brain_status"] = "READY"
        assembled["brain_ready"] = True
        assembled["brain_version"] = self.VERSION

        self.status = "attached"

        return assembled


def create_engine():
    return ArticleBrainAttachmentEngine()

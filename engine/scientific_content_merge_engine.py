# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Scientific Content Merge Engine
Production v1.0.0
"""


class ScientificContentMergeEngine:

    VERSION = "1.0.0"

    def normalize(self, text):
        if not text:
            return ""

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        return "\n".join(lines)

    def remove_duplicates(self, text):

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        unique = []
        seen = set()

        for p in paragraphs:
            key = p[:80]

            if key not in seen:
                seen.add(key)
                unique.append(p)

        return "\n\n".join(unique)

    def merge(self, old_content, deep_content):

        old_content = self.normalize(old_content)
        deep_content = self.normalize(deep_content)

        merged = ""

        if old_content:
            merged += old_content

        if deep_content:
            if merged:
                merged += "\n\n"

            merged += deep_content

        return self.remove_duplicates(merged)

    def info(self):

        return {
            "engine": "Scientific Content Merge Engine",
            "version": self.VERSION,
            "status": "production",
        }

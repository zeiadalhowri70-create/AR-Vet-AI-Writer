# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Scientific Expansion Knowledge Fallback Engine
Production v3.0.0
"""

import json
from pathlib import Path

from engine.scientific_deep_knowledge_resolver import ScientificDeepKnowledgeResolver
from engine.scientific_content_merge_engine import ScientificContentMergeEngine


class ScientificExpansionKnowledgeFallbackEngine:

    VERSION = "3.0.0"

    def __init__(self):
        self.base = Path("knowledge/disease_profiles")
        self.deep_resolver = ScientificDeepKnowledgeResolver()
        self.merge_engine = ScientificContentMergeEngine()

    def load_profile(self, topic):

        for file in self.base.glob("*.json"):
            try:
                data = json.loads(file.read_text(encoding="utf-8"))

                names = [
                    str(data.get("name_ar", "")),
                    str(data.get("name_en", "")),
                    str(data.get("id", "")),
                ]

                if any(topic.lower() in n.lower() for n in names):
                    return data

            except Exception:
                continue

        return {}

    def expand(self, section, content, topic=None):

        profile = self.load_profile(topic or "")

        result = content.strip()

        deep = self.deep_resolver.resolve(section, profile, topic or "")

        if deep:
            result = self.merge_engine.merge(result, deep)

        # Remove duplicated expansion blocks
        blocks = result.split("\n\n")
        unique = []

        for block in blocks:
            clean = block.strip()
            if clean and clean not in unique:
                unique.append(clean)

        result = "\n\n".join(unique)

        scientific = profile.get("scientific_profile", {})

        parts = []

        if section == "الأعراض السريرية":

            signs = scientific.get("clinical_signs", [])

            if signs:
                parts.append("تشمل العلامات السريرية: " + "، ".join(signs))

        elif section == "التشخيص":

            diagnosis = scientific.get("diagnosis", {})

            for key, value in diagnosis.items():

                if value:
                    parts.append(f"{key}: " + "، ".join(value))

        if parts:
            result += "\n\n" + "\n\n".join(parts)

        return result

    def info(self):

        return {
            "engine": "Scientific Expansion Knowledge Fallback Engine",
            "version": self.VERSION,
            "status": "production",
        }

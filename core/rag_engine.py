# -*- coding: utf-8 -*-

"""
Veterinary RAG Engine
AR-Vet AI Writer

Stage 3.1.2.B
"""

from pathlib import Path
import json

from core.context_map import ContextMap


class RAGEngine:

    def __init__(self):

        self.profile_folder = Path("knowledge/disease_profiles")
        self.context_map = ContextMap()

    def load_profile(self, disease_id):

        file = self.profile_folder / f"{disease_id}.json"

        if not file.exists():
            return None

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def build_context(self, disease_id, section_title=""):

        profile = self.load_profile(disease_id)

        if profile is None:
            return {}

        scientific = profile.get("scientific_profile", {})

        keys = self.context_map.get(section_title)

        context = {}

        for key in keys:
            if key in scientific:
                context[key] = scientific[key]
            elif key in profile:
                context[key] = profile[key]

        return context

    def info(self):

        profiles = list(self.profile_folder.glob("*.json"))

        return {
            "engine": "Veterinary RAG Engine",
            "version": "3.1.2",
            "profiles": len(profiles),
            "mapped_sections": self.context_map.info()["sections"],
        }

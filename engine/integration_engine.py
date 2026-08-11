# -*- coding: utf-8 -*-

"""
Integration Engine
AR-Vet AI Writer
Stage 6.4.2
"""

from engine.ai_writer import AIWriter
from engine.html_builder import HTMLBuilder
from core.reference_manager import ReferenceManager


class IntegrationEngine:

    def __init__(self):

        self.ai_writer = AIWriter()

        self.html_builder = HTMLBuilder()

        self.reference_manager = ReferenceManager(self.load_references())

    def load_references(self):

        import json

        try:

            with open("knowledge/references.json", "r", encoding="utf-8") as f:

                return json.load(f)

        except Exception:

            return {}

    def generate_article(self, project, part):

        # توليد المحتوى
        content = self.ai_writer.generate(project, part)

        # إضافة المراجع
        references = self.reference_manager.build_reference_html()

        content = content + "\n" + references

        # بناء HTML النهائي
        html = self.html_builder.build(project, part, content)

        filename = f"{project.name}_part_{part.number}.html"

        from pathlib import Path

        folder = Path("articles")

        folder.mkdir(exist_ok=True)

        file_path = folder / filename

        with open(file_path, "w", encoding="utf-8") as f:

            f.write(html)

        return {"file": str(file_path), "html": html, "content": content}

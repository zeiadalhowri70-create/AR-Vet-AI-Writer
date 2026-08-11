# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Article Real Content Builder Engine

Encyclopedia Edition v2.0

Production Final
"""

from engine.encyclopedia_engine_registry import EncyclopediaEngineRegistry
from core.article_writer_adapter_bridge import ArticleWriterAdapterBridge
from platform_core.registry.veterinary_brain_registry_binding import (
    VeterinaryBrainRegistryBinding,
)
from engine.content_quality_engine import ContentQualityEngine
from engine.reference_writer_engine import ReferenceWriterEngine
from engine.article_references_data_engine import ArticleReferencesDataEngine
from engine.article_citation_writer_engine import ArticleCitationWriterEngine
from engine.article_content_recovery_engine import ArticleContentRecoveryEngine
from engine.scientific_expansion_engine import ScientificExpansionEngine
from engine.scientific_expansion_validation_engine import (
    ScientificExpansionValidationEngine,
)
from engine.scientific_expansion_executor_engine import (
    ScientificExpansionExecutorEngine,
)
from engine.article_specification import ArticleSpecification


class ArticleRealContentBuilderEngine:

    VERSION = "2.0.0"

    def __init__(self, veterinary_brain=None):

        self.registry = EncyclopediaEngineRegistry()
        self.writer_bridge = ArticleWriterAdapterBridge()
        if veterinary_brain:
            self.veterinary_brain = veterinary_brain
        else:
            self.veterinary_brain = VeterinaryBrainRegistryBinding().build()["integration"]

        self.specification = ArticleSpecification()
        self.quality = ContentQualityEngine()
        self.scientific_expansion = ScientificExpansionEngine()
        self.scientific_expansion_validator = ScientificExpansionValidationEngine()
        self.scientific_expansion_executor = ScientificExpansionExecutorEngine()

        self.references = ReferenceWriterEngine()
        self.references_data = ArticleReferencesDataEngine()

        self.citations = ArticleCitationWriterEngine()
        self.recovery = ArticleContentRecoveryEngine()

    def _extract_content(self, result):

        if isinstance(result, dict):
            return result.get("content", "")

        return result

    def _write_engine(self, engine, topic, context=None):

        try:
            if context:
                return engine.write(topic, context)
        except TypeError:
            pass

        return engine.write(topic)

    def build_faq(self, topic):

        return [
            {"question": f"ما هو {topic}؟", "answer": f"شرح موسوعي عن {topic}."},
            {
                "question": f"كيف تتم الوقاية من {topic}؟",
                "answer": "تعتمد الوقاية على التشخيص المبكر والأمن الحيوي والتحصين.",
            },
        ]

    def build(self, topic, context=None):

        if context is None:
            context = {}

        brain_case = {
            "animal": "poultry",
            "disease": topic,
            "symptoms": context.get("symptoms", []),
        }

        context["veterinary_brain"] = self.veterinary_brain.execute(brain_case)

        sections = []

        for title, engine in self.registry.get_engines():

            result = self.writer_bridge.execute(
                engine,
                topic,
                context
            )

            content = self._extract_content(result)

            if not content or len(str(content).strip()) < 100:
                content = self.recovery.recover(title, topic, context)

            expansion_plan = self.scientific_expansion.create_expansion_plan(title)

            sections.append(
                {
                    "title": title,
                    "content": content,
                    "engine": engine.__class__.__name__,
                    "validated": True,
                    "expansion_plan": expansion_plan,
                }
            )

        sections = self.scientific_expansion_executor.execute(sections)

        disease_id = context.get("disease_id", "") if context else ""

        references = []

        if disease_id:
            references = self.references_data.get_references(disease_id)

        if not references:
            references = self._extract_content(
                self.references.write(topic, context)
            )

        citations = self._extract_content(self.citations.write(topic))

        quality = {}

        for section in sections:

            quality[section["title"]] = self.quality.review_section(
                section["title"], section["content"]
            )

        expansion_validation = self.scientific_expansion_validator.validate_sections(
            sections
        )

        return {
            "title": topic,
            "sections": sections,
            "expansion_validation": expansion_validation,
            "sections_count": len(sections),
            "encyclopedia": True,
            "version": self.VERSION,
            "faq": self.build_faq(topic),
            "references": references,
            "citations": citations,
            "quality": quality,
            "article_specification": self.specification.get(),
        }

    def info(self):

        return {
            "engine": "Article Real Content Builder Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Builder",
            "sections_dynamic": True,
            "status": "production",
        }

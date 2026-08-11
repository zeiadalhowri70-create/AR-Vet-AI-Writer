# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Scientific Expansion Executor Engine
Production Final v1.0.0
"""

from copy import deepcopy
from engine.scientific_expansion_ai_adapter import ScientificExpansionAIAdapter
from engine.scientific_expansion_knowledge_fallback_engine import (
    ScientificExpansionKnowledgeFallbackEngine,
)


class ScientificExpansionExecutorEngine:
    VERSION = "1.2.0"

    def execute(self, sections):
        """
        ينفذ خطة التوسعة العلمية لكل قسم دون كسر البنية الحالية.
        """

        expanded = []
        ai_adapter = ScientificExpansionAIAdapter()
        knowledge_fallback = ScientificExpansionKnowledgeFallbackEngine()

        for section in sections:
            item = deepcopy(section)
            fallback_used = False

            plan = item.get("expansion_plan", {})

            target = int(plan.get("target_words", 0))

            content = item.get("content", "") or ""

            if target > len(content.split()):
                ai_content = ai_adapter.expand(item.get("title", ""), content, target)

                if (
                    isinstance(ai_content, str)
                    and len(ai_content.split()) > len(content.split())
                    and not ai_content.startswith("تعذر إنشاء")
                ):
                    content = ai_content

                elif isinstance(ai_content, str) and ai_content.startswith(
                    "تعذر إنشاء"
                ):

                    knowledge_content = knowledge_fallback.expand(
                        item.get("title", ""), content, item.get("topic", "")
                    )

                    if isinstance(knowledge_content, str) and len(
                        knowledge_content.split()
                    ) > len(content.split()):
                        content = knowledge_content
                        fallback_used = True

            current = len(content.split())

            if target > current and not fallback_used:
                retry_content = knowledge_fallback.expand(
                    item.get("title", ""), content, item.get("topic", "")
                )

                if (
                    isinstance(retry_content, str)
                    and len(retry_content.split()) > current
                    and retry_content.strip() != content.strip()
                ):
                    if retry_content.count(content.strip()) <= 1:
                        content = retry_content

            item["content"] = content
            item["expanded"] = True
            item["final_words"] = len(content.split())

            expanded.append(item)

        return expanded

    def info(self):
        return {
            "engine": "Scientific Expansion Executor Engine",
            "version": self.VERSION,
            "type": "Production Final",
        }


if __name__ == "__main__":
    engine = ScientificExpansionExecutorEngine()

    sample = [
        {
            "title": "اختبار",
            "content": "كلمات قليلة",
            "expansion_plan": {"target_words": 100},
        }
    ]

    result = engine.execute(sample)

    assert result[0]["expanded"] is True
    assert result[0]["final_words"] >= 100

    print(engine.info())
    print("✅ ScientificExpansionExecutorEngine Production Final TEST PASSED")

# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer

Builder Bridge Integration Test

Stage B.3.4.1
"""

from engine.article_real_content_builder_engine import ArticleRealContentBuilderEngine
from core.article_writer_adapter_bridge import ArticleWriterAdapterBridge
from core.writer_context_bridge import WriterContextBridge


def main():

    topic = "مرض النيوكاسل في الدواجن"

    builder = ArticleRealContentBuilderEngine()

    bridge = ArticleWriterAdapterBridge()

    context = WriterContextBridge().prepare("newcastle_disease")

    writers = [
        ("definition", builder.definition),
    ]

    print("=" * 70)
    print("AR-VET BUILDER BRIDGE TEST B.3.4.1")
    print("=" * 70)

    for name, writer in writers:

        result = bridge.execute(writer, topic, context)

        print(name, "OK:", bool(result.get("content")))

        print("length:", len(result.get("content", "")))

    print("=" * 70)
    print("✅ B.3.4.1 COMPLETE")


if __name__ == "__main__":
    main()

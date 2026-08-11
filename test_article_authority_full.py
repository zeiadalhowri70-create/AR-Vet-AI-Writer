# -*- coding: utf-8 -*-

from engine.article_writer_integration_engine import ArticleWriterIntegrationEngine

topic = "مرض النيوكاسل في الدواجن"

print("=" * 70)
print("AR-VET FULL ENCYCLOPEDIA AUTHORITY TEST")
print("=" * 70)

engine = ArticleWriterIntegrationEngine()

article = engine.generate(topic)

print("\nTITLE:")
print(article.get("title"))

print("\nSECTIONS:")
print(article.get("sections_count"))

for section in article.get("sections", []):
    print("-", section.get("title"), "|", section.get("engine"))

print("\nAUTHORITY:")
print(article.get("scientific_authority"))

print("\nQUALITY:")
print(article.get("quality_score"))

print("\nEXPANSION:")
print(article.get("scientific_expansion_validation_summary"))

print("\nREADY:")
print(article.get("publishing_readiness"))

print("=" * 70)

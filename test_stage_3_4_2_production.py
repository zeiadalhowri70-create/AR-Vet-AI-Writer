# -*- coding: utf-8 -*-

print("=" * 70)
print("AR-Vet AI Writer")
print("Stage 3.4.2 Production Audit")
print("=" * 70)


tests = []


def check(name, func):

    try:
        result = func()

        print("\n✅", name)
        print(result)

        tests.append({"name": name, "status": "PASS"})

    except Exception as e:

        print("\n❌", name)
        print(e)

        tests.append({"name": name, "status": "FAIL"})


# 1 Content Quality

check(
    "Content Quality Engine",
    lambda: __import__(
        "engine.content_quality_engine", fromlist=["ContentQualityEngine"]
    )
    .ContentQualityEngine()
    .info(),
)


# 2 Real Content Builder

check(
    "Article Real Content Builder",
    lambda: __import__(
        "engine.article_real_content_builder_engine",
        fromlist=["ArticleRealContentBuilderEngine"],
    )
    .ArticleRealContentBuilderEngine()
    .info(),
)


# 3 Scientific Validation

check(
    "Scientific Validation",
    lambda: __import__(
        "engine.article_scientific_validation_engine",
        fromlist=["ArticleScientificValidationEngine"],
    )
    .ArticleScientificValidationEngine()
    .info(),
)


# 4 Quality Writer

check(
    "Quality Writer",
    lambda: __import__(
        "engine.article_quality_writer_engine", fromlist=["ArticleQualityWriterEngine"]
    )
    .ArticleQualityWriterEngine()
    .info(),
)


# 5 Language Writer

check(
    "Language Writer",
    lambda: __import__(
        "engine.article_language_writer_engine",
        fromlist=["ArticleLanguageWriterEngine"],
    )
    .ArticleLanguageWriterEngine()
    .info(),
)


# 6 Style Writer

check(
    "Style Writer",
    lambda: __import__(
        "engine.article_style_writer_engine", fromlist=["ArticleStyleWriterEngine"]
    )
    .ArticleStyleWriterEngine()
    .info(),
)


print("\n")
print("=" * 70)
print("FINAL REPORT")
print("=" * 70)


passed = 0

for t in tests:

    print(t["status"], "-", t["name"])

    if t["status"] == "PASS":
        passed += 1


print()
print("SUCCESS:", passed, "/", len(tests))

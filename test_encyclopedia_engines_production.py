from engine.encyclopedia_engine_registry import EncyclopediaEngineRegistry

topic = "مرض النيوكاسل في الدواجن"

registry = EncyclopediaEngineRegistry()

print("=" * 70)
print("AR-VET ENCYCLOPEDIA ENGINE PRODUCTION TEST")
print("=" * 70)

passed = 0
failed = 0

for title, engine in registry.get_engines():

    try:
        result = engine.write(topic)

        if isinstance(result, dict):
            content = result.get("content", "")
        else:
            content = result

        length = len(str(content))

        if length >= 100:
            print("PASS:", title, "|", engine.__class__.__name__, "|", length)
            passed += 1
        else:
            print("FAIL:", title, "| EMPTY CONTENT")
            failed += 1

    except Exception as e:
        print("ERROR:", title, "|", str(e))
        failed += 1

print("=" * 70)
print("PASSED:", passed)
print("FAILED:", failed)
print("=" * 70)

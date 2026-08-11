from pathlib import Path

target = Path("engine/article_real_content_builder_engine.py")

txt = target.read_text(encoding="utf-8")

changes = 0

if "from core.article_writer_adapter_bridge import ArticleWriterAdapterBridge" not in txt:
    txt = txt.replace(
        "from engine.encyclopedia_engine_registry import EncyclopediaEngineRegistry",
        "from engine.encyclopedia_engine_registry import EncyclopediaEngineRegistry\nfrom core.article_writer_adapter_bridge import ArticleWriterAdapterBridge"
    )
    changes += 1

if "self.writer_bridge = ArticleWriterAdapterBridge()" not in txt:
    txt = txt.replace(
        "self.registry = EncyclopediaEngineRegistry()",
        "self.registry = EncyclopediaEngineRegistry()\n        self.writer_bridge = ArticleWriterAdapterBridge()"
    )
    changes += 1

old = "result = self._write_engine(engine, topic, context)"

new = """result = self.writer_bridge.execute(
                engine,
                topic,
                context
            )"""

if old in txt:
    txt = txt.replace(old, new)
    changes += 1

if changes == 0:
    print("C34.1 PATCH NOT APPLIED - ALREADY EXISTS")
else:
    target.write_text(txt, encoding="utf-8")
    print("C34.1 WRITER BRIDGE PATCH OK")
    print("CHANGES:", changes)

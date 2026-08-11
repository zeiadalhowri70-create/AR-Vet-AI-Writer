# -*- coding: utf-8 -*-

from pathlib import Path


class ArticleExportEngine:
    """
    يصدر المقال النهائي كملف HTML.
    """

    def __init__(self):
        self.version = "1.0"
        self.output_folder = Path("output")

    def export(self, article):
        self.output_folder.mkdir(exist_ok=True)

        title = article.get("title", "article")

        filename = title.replace(" ", "_").replace("/", "_") + ".html"

        path = self.output_folder / filename

        html = article.get("html", "")

        path.write_text(html, encoding="utf-8")

        return {"file": str(path), "size": len(html), "status": "exported"}

    def info(self):
        return {
            "engine": "Article Export Engine",
            "version": self.version,
            "status": "production",
        }

# -*- coding: utf-8 -*-

from pathlib import Path


class BloggerArticleExportEngine:

    def export(self, article):

        if isinstance(article, str):
            html = Path(article).read_text(encoding="utf-8")
            title = Path(article).stem.replace("_", " ")
        else:
            title = article.get("title", "AR-Vet Article")
            html = article.get("content", "")

        out = "output/blogger_draft.html"

        Path(out).write_text(html, encoding="utf-8")

        return {"title": title, "file": out, "html_ready": True, "content": html}

    def info(self):

        return {
            "engine": "Blogger Article Export Engine",
            "version": "2.0",
            "status": "production",
        }

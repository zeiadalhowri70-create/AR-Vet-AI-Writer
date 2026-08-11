# -*- coding: utf-8 -*-

import re


class ArticleTOCEngine:

    VERSION = "1.0"

    def build(self, html):

        headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html, flags=re.IGNORECASE)

        if not headings:
            return ""

        toc = ['<nav id="table-of-contents">', "<h2>جدول المحتويات</h2>", "<ul>"]

        for anchor, title in headings:
            toc.append(f'<li><a href="#{anchor}">{title}</a></li>')

        toc.extend(["</ul>", "</nav>"])

        return "\n".join(toc)

    def info(self):
        return {
            "engine": "Article TOC Engine",
            "version": self.VERSION,
            "status": "production",
            "auto_detect": True,
            "anchors": True,
        }

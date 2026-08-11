# -*- coding: utf-8 -*-

import re


class ArticleHTMLSanitizationEngine:

    def __init__(self):
        self.version = "1.0.0"

    def sanitize(self, html):

        if not html:
            return ""

        html = str(html)

        replacements = {
            "<br>": "<br/>",
            "<br >": "<br/>",
            "</br>": "",
            "&nbsp;": " ",
        }

        for old, new in replacements.items():
            html = html.replace(old, new)

        allowed_remove = [
            r"<section[^>]*>",
            r"</section>",
            r"<article[^>]*>",
            r"</article>",
            r"<para[^>]*>",
            r"</para>",
        ]

        for pattern in allowed_remove:
            html = re.sub(pattern, "", html, flags=re.I)

        html = re.sub(
            r'<script(?![^>]*type=["\']application/ld\+json["\'])[^>]*>.*?</script>',
            "",
            html,
            flags=re.I | re.S,
        )

        html = re.sub(
            r'<style[^>]*>.*?</style>',
            "",
            html,
            flags=re.I | re.S,
        )

        return html.strip()

    def validate(self, html):

        if not html:
            return False

        return "<br>" not in html and "</br>" not in html

    def process(self, html):

        cleaned = self.sanitize(html)

        return {
            "html": cleaned,
            "valid": self.validate(cleaned),
            "engine": "Article HTML Sanitization Engine",
            "version": self.version,
        }

    def info(self):

        return {
            "engine": "Article HTML Sanitization Engine",
            "version": self.version,
            "status": "production",
        }

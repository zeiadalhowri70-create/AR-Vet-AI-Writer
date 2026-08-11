# -*- coding: utf-8 -*-

"""
Content Cleaner
AR-Vet AI Writer

Stage : 3.4.2.4
Version : 2.0
"""

import re


class ContentCleaner:

    def clean(self, text):

        if text is None:
            return ""

        text = str(text)

        # إزالة Markdown
        text = text.replace("**", "")
        text = text.replace("__", "")
        text = text.replace("```", "")
        text = text.replace("`", "")

        # إزالة المسافات الزائدة
        text = re.sub(r"[ \t]+", " ", text)

        # إزالة أكثر من سطر فارغ
        text = re.sub(r"\n{3,}", "\n\n", text)

        # إزالة الفراغات قبل وبعد السطر
        lines = [line.strip() for line in text.splitlines()]
        text = "\n".join(lines)

        # تحويل العناوين
        text = re.sub(r"^###\s*(.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)

        text = re.sub(r"^##\s*(.+)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)

        text = re.sub(r"^#\s*(.+)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)

        html = []

        for block in text.split("\n\n"):

            block = block.strip()

            if not block:
                continue

            if block.startswith("<h"):
                html.append(block)
            else:
                html.append(f"<p>{block}</p>")

        return "\n".join(html)

    def info(self):

        return {"engine": "Content Cleaner", "version": "2.0", "status": "production"}

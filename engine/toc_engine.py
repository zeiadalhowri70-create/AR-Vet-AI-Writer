# -*- coding: utf-8 -*-


class TOCEngine:
    """
    AR-Vet AI Writer
    Table Of Contents Engine
    Version 2.0
    """

    DEFAULT_SECTIONS = [
        ("introduction", "المقدمة"),
        ("definition", "التعريف"),
        ("causes", "الأسباب"),
        ("symptoms", "الأعراض"),
        ("diagnosis", "التشخيص"),
        ("treatment", "العلاج"),
        ("prevention", "الوقاية"),
        ("control", "المكافحة"),
        ("conclusion", "الخاتمة"),
    ]

    def build(self, sections=None):

        sections = sections or self.DEFAULT_SECTIONS

        html = ['<div class="toc">', "<h2>جدول المحتويات</h2>", "<ul>"]

        for anchor, title in sections:
            html.append(f'<li><a href="#{anchor}">{title}</a></li>')

        html.extend(["</ul>", "</div>"])

        return "\n".join(html)

    def info(self):

        return {
            "engine": "TOC Engine",
            "version": "2.0",
            "status": "production",
            "automatic": True,
            "sections": len(self.DEFAULT_SECTIONS),
        }

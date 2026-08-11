# -*- coding: utf-8 -*-

from engine.html_processor import HTMLProcessor


class ArticleContentAssemblyEngine:

    SECTION_ORDER = [
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

    def __init__(self):
        self.processor = HTMLProcessor()

    def _normalize(self, value):

        if value is None:
            return ""

        if isinstance(value, str):
            return value.strip()

        if isinstance(value, dict):
            for key in ("content", "text", "response"):
                if isinstance(value.get(key), str):
                    return value[key].strip()

        return str(value).strip()

    def assemble(self, article):

        html = []

        # دعم البنية الحديثة sections
        if article.get("sections"):
            for section in article.get("sections", []):
                title = section.get("title", "")
                content = self._normalize(section.get("content", ""))

                if not content:
                    continue

                html.append(f"<h2>{title}</h2>")
                html.append(self.processor.process(content))

        # دعم البنية القديمة
        else:
            for key, heading in self.SECTION_ORDER:
                content = self._normalize(article.get(key))

                if not content:
                    continue

                html.append(f'<h2 id="{key}">{heading}</h2>')
                html.append(self.processor.process(content))

        if article.get("references"):

            html.append("<section class='references'>")
            html.append("<h2>المراجع العلمية</h2>")
            html.append(self.processor.process(self._normalize(article["references"])))
            html.append("</section>")

        if article.get("citations"):

            html.append("<section class='citations'>")
            html.append("<h2>الاستشهادات</h2>")
            html.append(self.processor.process(self._normalize(article["citations"])))
            html.append("</section>")

        assembled = article.copy()

        assembled.update(
            {
                "title": self._normalize(article.get("title")),
                "content": "\n".join(html),
                "sections": article.get("sections", []),
                "assembled": True,
            }
        )

        return assembled

    def info(self):
        return {
            "engine": "Article Content Assembly Engine",
            "version": "7.0",
            "status": "production",
            "processor": "HTMLProcessor",
            "references": True,
            "citations": True,
            "toc": False,
            "title": False,
        }

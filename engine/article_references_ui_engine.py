# -*- coding: utf-8 -*-


class ArticleReferencesUIEngine:
    VERSION = "1.1"

    def build(self, article):
        refs = article.get("references")

        if isinstance(refs, str):
            refs = [refs]

        if not refs:
            refs = [
                {
                    "organization": "WOAH",
                    "title": "World Organisation for Animal Health",
                    "url": "https://www.woah.org",
                },
                {
                    "organization": "FAO",
                    "title": "Food and Agriculture Organization",
                    "url": "https://www.fao.org",
                },
                {
                    "organization": "Merck",
                    "title": "Merck Veterinary Manual",
                    "url": "https://www.merckvetmanual.com",
                },
            ]

        html = [
            '<section id="references-ui" class="reference-section">',
            '<h2><i class="fas fa-book"></i> المراجع العلمية الأكاديمية</h2>',
            '<ol class="references-list">',
        ]

        for ref in refs:
            if isinstance(ref, dict):
                org = ref.get("organization", "مصدر علمي")
                title = ref.get("title", "مرجع طبي بيطري")
                url = ref.get("url", "#")
                html.append(
                    f'<li><strong>{org}</strong>: <a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a></li>'
                )
            else:
                # في حال كان المرجع نصاً عادياً وليس قاموساً
                html.append(f"<li>{ref}</li>")

        html.append("</ol>")
        html.append("</section>")

        return "\n".join(html)

    def info(self):
        return {
            "engine": "Article References UI Engine",
            "version": self.VERSION,
            "status": "production",
        }

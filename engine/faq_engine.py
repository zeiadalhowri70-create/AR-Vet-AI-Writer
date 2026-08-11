# -*- coding: utf-8 -*-

import json


class FAQEngine:

    def __init__(self):
        pass

    def build_html(self, items):

        html = "<section class='faq'>"
        html += "<h2>الأسئلة الشائعة</h2>"

        for item in items:
            html += f"""
<div class="faq-item">
<h3>{item['question']}</h3>
<p>{item['answer']}</p>
</div>
"""

        html += "</section>"

        return html

    def build_schema(self, items):

        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [],
        }

        for item in items:

            schema["mainEntity"].append(
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
            )

        return schema

    def schema_script(self, items):

        return (
            '<script type="application/ld+json">\n'
            + json.dumps(self.build_schema(items), ensure_ascii=False, indent=4)
            + "\n</script>"
        )

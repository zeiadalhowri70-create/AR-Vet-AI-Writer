# -*- coding: utf-8 -*-
import json
from datetime import datetime


class ArticleSchemaEngine:
    """
    ينشئ JSON-LD Schema طبي بيطري متطور يدعم الكائنات والنصوص بشكل آمن.
    """

    def __init__(self):
        self.version = "1.1"

    def build(self, article):
        title = article.get("title", "")
        url = article.get("url", "")

        # استخراج اسم المؤلف بأمان سواء كان نصاً أو قاموساً تفصيلياً
        author_data = article.get("author", "الدكتور زياد الحوري")
        if isinstance(author_data, dict):
            author_name = author_data.get("name", "الدكتور زياد الحوري")
        else:
            author_name = str(author_data)

        schema = {
            "@context": "https://schema.org",
            "@type": "MedicalWebPage",
            "headline": title,
            "author": {"@type": "Person", "name": author_name},
            "publisher": {
                "@type": "Organization",
                "name": "مدونة الدكتور زياد الحوري البيطرية",
            },
            "datePublished": datetime.now().strftime("%Y-%m-%d"),
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": url if url else "https://arvetinfo.blogspot.com",
            },
        }

        # إرجاع الـ JSON منسقاً بشكل نظيف ومعزول برمجياً داخل وسم الـ script
        return f'<script type="application/ld+json">\n{
            json.dumps(
                schema,
                ensure_ascii=False,
                indent=2)}\n</script>'

    def info(self):
        return {
            "engine": "Article Schema Engine",
            "version": self.version,
            "status": "production",
        }

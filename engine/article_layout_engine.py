# -*- coding: utf-8 -*-
import re
from engine.article_css_engine import ArticleCSSEngine
from engine.article_toc_engine import ArticleTOCEngine
from engine.article_author_box_engine import ArticleAuthorBoxEngine
from engine.article_reading_experience_engine import ArticleReadingExperienceEngine
from engine.article_metadata_bar_engine import ArticleMetadataBarEngine
from engine.article_social_share_engine import ArticleSocialShareEngine
from engine.article_navigation_engine import ArticleNavigationEngine
from engine.article_medical_alert_engine import ArticleMedicalAlertEngine
from engine.article_schema_engine import ArticleSchemaEngine
from engine.article_seo_meta_engine import ArticleSEOMetaEngine
from engine.article_image_placeholder_engine import ArticleImagePlaceholderEngine
from engine.article_cover_image_engine import ArticleCoverImageEngine
from engine.article_related_articles_engine import ArticleRelatedArticlesEngine
from engine.article_references_ui_engine import ArticleReferencesUIEngine
import json


class ArticleLayoutEngine:
    VERSION = "1.4"

    def __init__(self):
        self.css = ArticleCSSEngine()
        self.toc = ArticleTOCEngine()
        self.author = ArticleAuthorBoxEngine()
        self.reading = ArticleReadingExperienceEngine()
        self.metadata_bar = ArticleMetadataBarEngine()
        self.social = ArticleSocialShareEngine()
        self.related = ArticleRelatedArticlesEngine()
        self.references_ui = ArticleReferencesUIEngine()
        self.related_articles = ArticleRelatedArticlesEngine()
        self.social_share = ArticleSocialShareEngine()
        self.navigation = ArticleNavigationEngine()
        self.medical_alerts = ArticleMedicalAlertEngine()
        self.schema_engine = ArticleSchemaEngine()
        self.seo_meta = ArticleSEOMetaEngine()
        self.image_placeholder = ArticleImagePlaceholderEngine()
        self.cover_image = ArticleCoverImageEngine()
        self.author_box = ArticleAuthorBoxEngine()

    def build(self, article):
        title = article.get("title", "")
        content = article.get("scientific_content", article.get("content", ""))

        if isinstance(content, str):
            content = content.replace("### ", "<h3>").replace(" ###", "</h3>")
            content = content.replace("## ", "<h2>").replace(" ##", "</h2>")
            content = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", content)
            content = content.replace("\n", "<br/>")

        # SEO meta description
        seo_meta = article.get("seo_meta", {})
        description = seo_meta.get(
            "description",
            f"مقال علمي بيطري متخصص حول {title} - معلومات شاملة عن الأعراض والتشخيص والعلاج والوقاية",
        )
        canonical_url = f"https://arvetinfo.blogspot.com/{
            title.replace(
                ' ', '-')}"

        # Schema JSON-LD (Article)
        schema_article = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description,
            "author": {"@type": "Person", "name": "د. زياد الحوري"},
            "publisher": {
                "@type": "Organization",
                "name": "AR-Vet Info",
                "url": "https://arvetinfo.blogspot.com",
            },
            "inLanguage": "ar",
            "url": canonical_url,
        }

        # FAQ schema
        faq_items = article.get("faq_items", [])
        faq_schema_block = ""
        faq_html_block = ""

        if faq_items:
            faq_schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item.get("question", ""),
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item.get("answer", ""),
                        },
                    }
                    for item in faq_items
                ],
            }
            faq_schema_block = f'<script type="application/ld+json">{
                json.dumps(
                    faq_schema,
                    ensure_ascii=False,
                    indent=2)}</script>'

            faq_items_html = ""
            for item in faq_items:
                q = item.get("question", "")
                a = item.get("answer", "")
                faq_items_html += f"""
                <div class="faq-item">
                    <h3 class="faq-question">{q}</h3>
                    <p class="faq-answer">{a}</p>
                </div>"""

            faq_html_block = f"""
            <section class="faq-section" id="faq">
                <h2>الأسئلة الشائعة (FAQ)</h2>
                {faq_items_html}
            </section>"""

        # References
        references_html = (
            '<div class="reference-section"><h2>المراجع</h2><ul class="reference-list">'
        )
        refs = article.get("references", [])
        if refs:
            for r in refs:
                if isinstance(r, dict):
                    org = r.get("organization", "مصدر علمي")
                    t_title = r.get("title", "مرجع طبي")
                    url = r.get("url", "#")
                    references_html += f'<li class="reference-item"><strong>{org}</strong>: <a href="{url}" target="_blank" rel="noopener">{t_title}</a></li>'
        references_html += "</ul></div>"

        html_output = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical_url}">
    <script type="application/ld+json">{json.dumps(schema_article, ensure_ascii=False, indent=2)}</script>
    {faq_schema_block}
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, sans-serif; line-height: 1.8; color: #334155; max-width: 850px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #0284c7; border-bottom: 3px solid #0284c7; padding-bottom: 10px; font-size: 2rem; }}
        h2 {{ color: #16a34a; border-right: 4px solid #16a34a; padding-right: 10px; margin-top: 30px; }}
        h3 {{ color: #0f172a; margin-top: 20px; }}
        strong {{ color: #0f172a; }}
        .medical-alert {{ background-color: #fff1f2; border-right: 4px solid #f43f5e; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .reference-section {{ background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 20px; margin-top: 40px; border-radius: 8px; }}
        .reference-list {{ list-style: none; padding: 0; }}
        .reference-item {{ margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px dashed #cbd5e1; }}
        a {{ color: #0284c7; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .faq-section {{ background: #fff8e8; border-radius: 12px; padding: 25px; margin-top: 35px; }}
        .faq-section h2 {{ border: none; color: #92400e; }}
        .faq-item {{ margin-bottom: 20px; border-bottom: 1px dashed #e5c97a; padding-bottom: 15px; }}
        .faq-question {{ color: #78350f; margin-bottom: 5px; }}
        .faq-answer {{ color: #334155; margin: 0; }}
    </style>
</head>
<body>
    <article>
        <h1>{title}</h1>
        <div class="medical-alert">
            <strong>تنبيه طبي بيطري:</strong> يجب تأكيد التشخيص بواسطة الطبيب البيطري المختص قبل البدء في تطبيق أي بروتوكول علاجي للقطيع.
        </div>
        <div class="article-content">
            {content}
        </div>
        {faq_html_block}
        {references_html}
    </article>
</body>
</html>"""

        return html_output

    def info(self):
        return {
            "engine": "Article Layout Engine",
            "version": self.VERSION,
            "css": True,
            "toc": True,
            "author_box": True,
            "status": "production",
            "doctype": True,
            "schema_jsonld": True,
            "faq_schema": True,
            "seo_meta": True,
            "canonical": True,
        }

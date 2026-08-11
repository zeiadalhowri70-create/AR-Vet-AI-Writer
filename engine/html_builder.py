# -*- coding: utf-8 -*-

"""
HTML Builder
AR-Vet AI Writer
Version 1.1
Stage 6.3.4
"""

from engine.seo_engine import SEOEngine
from engine.schema_engine import SchemaEngine
from engine.faq_engine import FAQEngine
from engine.toc_engine import TOCEngine
from engine.article_generator import ArticleGenerator
from engine.series_link_engine import SeriesLinkEngine


class HTMLBuilder:

    def __init__(self):

        self.seo = SEOEngine()
        self.schema = SchemaEngine()
        self.faq = FAQEngine()
        self.toc = TOCEngine()
        self.article = ArticleGenerator()
        self.series_links = SeriesLinkEngine()

    def build(self, project, part, content, faq_items=None):

        if faq_items is None:
            faq_items = []

        # SEO
        seo = self.seo.build(part.title, content, project.keywords)

        # Article Schema
        schema = self.schema.build_article(
            title=part.title,
            description=seo["description"],
            author="د. زياد الحوري",
            publisher="مدونة الدكتور زياد الحوري البيطرية",
            image="cover.jpg",
            url="#",
        )

        schema_script = self.schema.build_script(schema)

        # Table of Contents
        toc = self.toc.generate([part.title])

        # FAQ
        faq_html = self.faq.build_html(faq_items)

        faq_schema = self.faq.schema_script(faq_items)

        # Series Navigation
        series_navigation = self.series_links.build_links(
            part.number, len(project.parts)
        )

        # Generate HTML
        html = self.article.generate(
            title=part.title,
            content=(toc + "\n" + content + "\n" + faq_html + "\n" + series_navigation),
            category=project.category,
            author="د. زياد الحوري",
            keywords=project.keywords,
        )

        # Inject SEO + Schema
        html = html.replace(
            "</head>",
            f"""
<meta name="description" content="{seo['description']}">
<meta name="keywords" content="{seo['keywords']}">

{schema_script}

{faq_schema}

</head>
""",
        )

        return html

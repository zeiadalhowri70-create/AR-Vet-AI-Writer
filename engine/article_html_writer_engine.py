# -*- coding: utf-8 -*-
import markdown
from engine.toc_engine import TOCEngine
from engine.seo_engine import SEOEngine
from engine.schema_engine import SchemaEngine
from engine.professional_html_template_engine import ProfessionalHTMLTemplateEngine


class ArticleHTMLWriterEngine:

    def __init__(self):
        self.toc = TOCEngine()
        self.seo = SEOEngine()
        self.schema = SchemaEngine()
        self.template = ProfessionalHTMLTemplateEngine()

    def render(
        self,
        title,
        content,
        faq_html="",
        canonical="",
        references=None,
        media_library=None,
        image=None,
        video=None
    ):
        toc = self.toc.build()

        seo = self.seo.build(
            title, content, keywords=[title, "الدواجن", "أمراض الدواجن", "طب بيطري"]
        )

        schema_data = self.schema.build_article(
            title=seo["title"],
            description=seo["description"],
            url=canonical if canonical else "",
        )
        schema_script = self.schema.build_script(schema_data)

        content_html = markdown.markdown(
            content, extensions=["extra", "nl2br"], output_format="html5"
        )

        final_body = toc + "\n" + content_html

        references_html = ""
        for ref in (references or []):
            if isinstance(ref, dict):
                references_html += f"""
                <p>
                <strong>{ref.get("organization","مصدر علمي")}</strong>
                :
                <a href="{ref.get("url","#")}" target="_blank">
                {ref.get("title","مرجع")}
                </a>
                </p>
                """

        media_library = media_library or {}

        video_html = ""
        if video and isinstance(video, dict):
            youtube_url = video.get("youtube_url", "")
            video_path = video.get("video_path", "")

            if youtube_url:
                video_html = f"""
                <section class="video-section">
                    <h2>فيديو تعليمي بيطري</h2>
                    <div class="video-card">
                        <iframe
                            src="{youtube_url.replace("watch?v=", "embed/")}"
                            title="فيديو تعليمي بيطري"
                            loading="lazy"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowfullscreen>
                        </iframe>
                    </div>
                </section>
                """
            elif video_path:
                video_html = f"""
                <section class="video-section">
                    <h2>فيديو تعليمي بيطري</h2>
                    <video controls preload="metadata" style="max-width:100%;width:100%;border-radius:12px;">
                        <source src="{video_path}" type="video/mp4">
                    </video>
                </section>
                """

        return self.template.render(
            title=seo["title"],
            body=final_body,
            description=seo["description"],
            canonical=canonical if canonical else "https://arvetinfo.blogspot.com/",
            schema_script=schema_script,
            faq_html=faq_html,
            references_html=references_html,
            media_library=media_library,
            video_html=video_html,
        )

    def info(self):
        return {
            "engine": "Article HTML Writer Engine",
            "version": "7.0",
            "status": "production",
            "professional_template": True,
            "seo": True,
            "schema": True,
            "toc": True,
            "faq": True,
            "canonical": True,
        }

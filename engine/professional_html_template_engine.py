# -*- coding: utf-8 -*-
class ProfessionalHTMLTemplateEngine:
    VERSION = "3.0"

    def render(
        self, title, body, description="", canonical="", schema_script="", faq_html="", references_html="", media_library=None, video_html=""
    ):
        meta_description = description if description else title
        canonical_url = canonical if canonical else "https://arvetinfo.blogspot.com/"

        media_library = media_library or {}

        media_html = ""

        media = media_library.get("media", {})

        featured = media.get("featured_image", {})

        if featured.get("path"):
            media_html += f"""
            <div class="card">
                <h2>الصورة التشريحية الرئيسية</h2>
                <img src="{featured.get("path")}" 
                     alt="المظاهر التشريحية للمرض"
                     style="max-width:100%;border-radius:12px;">
            </div>
            """

        images = media.get("anatomical_images", [])

        if images:
            media_html += """
            <div class="card">
            <h2>صور المظاهر التشريحية</h2>
            """

            for img in images:
                if img.get("path"):
                    media_html += f"""
                    <img src="{img.get("path")}"
                         alt="gross lesion"
                         style="max-width:100%;margin:10px;border-radius:12px;">
                    """

            media_html += "</div>"

        return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{title}</title>
    <meta name="description" content="{meta_description}">
    <meta name="robots" content="index,follow">
    <link rel="canonical" href="{canonical_url}">

    {schema_script}

    <style>
    * {{
        box-sizing:border-box;
    }}
    body {{
        margin:0;
        padding:0;
        background:#f4f7f9;
        font-family:Tahoma,Arial,sans-serif;
        direction:rtl;
        line-height:2;
    }}
    .site-header {{
        background:#146c43;
        color:white;
        padding:25px;
        text-align:center;
    }}
    .container {{
        width:100%;
        max-width:1100px;
        margin:auto;
        padding:20px;
    }}
    article {{
        background:white;
        padding:35px;
        border-radius:16px;
        box-shadow:0 5px 25px rgba(0,0,0,.08);
    }}
    h1 {{
        font-size:36px;
        color:#146c43;
        margin-top:0;
    }}
    h2 {{
        font-size:27px;
        color:#0d6efd;
        margin-top:45px;
        border-bottom:2px solid #eee;
        padding-bottom:10px;
    }}
    h3 {{
        color:#146c43;
    }}
    p {{
        font-size:18px;
        text-align:justify;
    }}
    .card {{
        background:#f8fafc;
        border-right:5px solid #146c43;
        padding:20px;
        margin:25px 0;
        border-radius:12px;
    }}
    .faq-box {{
        background:#fff8e8;
        padding:20px;
        border-radius:12px;
        margin-top:30px;
    }}
    .references {{
        background:#eef6ff;
        padding:20px;
        border-radius:12px;
    }}
    .actions {{
        display:flex;
        gap:10px;
        flex-wrap:wrap;
        margin:20px 0;
    }}
    .button {{
        padding:10px 18px;
        background:#146c43;
        color:white;
        border-radius:8px;
        text-decoration:none;
    }}
    .video-section {{
        margin:45px 0;
    }}
    .video-card {{
        position:relative;
        width:100%;
        max-width:100%;
        aspect-ratio:16/9;
        overflow:hidden;
        border-radius:16px;
        background:#111;
        box-shadow:0 5px 20px rgba(0,0,0,.12);
    }}
    .video-card iframe {{
        position:absolute;
        inset:0;
        width:100%;
        height:100%;
        border:0;
    }}
    .video-section video {{
        display:block;
        width:100%;
        max-width:100%;
        height:auto;
        border-radius:16px;
        background:#111;
    }}

    .ads-box {{
        min-height:100px;
        background:#fafafa;
        border:1px dashed #ccc;
        margin:30px 0;
        display:flex;
        align-items:center;
        justify-content:center;
    }}
    footer {{
        margin-top:50px;
        padding:25px;
        text-align:center;
        border-top:1px solid #ddd;
        color:#777;
    }}
    @media(max-width:700px) {{
        body {{ font-size:15px; }}
        .container {{ padding:10px; }}
        article {{ padding:20px; }}
        h1 {{ font-size:28px; }}
        h2 {{ font-size:22px; }}
        p {{ font-size:16px; }}
    }}
    </style>
</head>

<body>

<header class="site-header">
    <h2>مدونة الدكتور زياد الحوري البيطرية</h2>
    <p>AR-Vet AI Veterinary Intelligence</p>
</header>

<div class="container">

    <div class="actions">
        <a class="button">مشاركة</a>
        <a class="button">طباعة</a>
        <a class="button">PDF</a>
    </div>

    <div class="ads-box">
        AdSense Placeholder
    </div>

    <article>
        <h1>{title}</h1>
        {body}

        {media_html}

{video_html}

        <div class="card">
            <b>نصيحة الطبيب:</b>
            <br/>
            استشر الطبيب البيطري قبل استخدام أي علاج.
        </div>

        <div class="faq-box">
            <h2>الأسئلة الشائعة</h2>
            {faq_html}
        </div>

        <div class="references">
            <h2>المراجع</h2>
            {references_html}
        </div>

    </article>

    <footer>
        تم الإنشاء بواسطة AR-Vet AI Writer
    </footer>

</div>

</body>
</html>"""

    def info(self):
        return {
            "engine": "Professional HTML Template Engine",
            "version": self.VERSION,
            "status": "production",
            "responsive": True,
            "mobile_first": True,
            "adsense_ready": True,
            "seo_ready": True,
        }

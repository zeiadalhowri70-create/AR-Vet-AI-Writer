from pathlib import Path

p = Path("engine/professional_html_template_engine.py")
txt = p.read_text(encoding="utf-8")

old = """<article>
{body}

<footer>"""

new = """<article>
{body}

<section class="arvet-author-box">
<h2>عن هذا المقال</h2>
<p><strong>آخر تحديث:</strong> {{LAST_UPDATE}}</p>
<p>تمت مراجعة هذا المحتوى بواسطة منصة AR-Vet AI Veterinary Intelligence.</p>
</section>

<section class="arvet-disclaimer">
<h2>تنبيه بيطري</h2>
<p>المعلومات الواردة لأغراض تعليمية ولا تغني عن الفحص السريري والتحاليل المخبرية واستشارة الطبيب البيطري.</p>
</section>

<footer>"""

txt = txt.replace(old, new)

txt = txt.replace(
    "font-size:14px;",
    """font-size:14px;
}

.arvet-author-box,.arvet-disclaimer{
margin-top:35px;
padding:20px;
border-radius:10px;
background:#f8f9fa;
border-right:5px solid #198754;
""",
)

txt = txt.replace("{{LAST_UPDATE}}", "2026-07-16")

p.write_text(txt, encoding="utf-8")

print("4.10.3.A PATCH OK")

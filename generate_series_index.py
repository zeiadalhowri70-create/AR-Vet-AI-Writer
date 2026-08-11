# -*- coding: utf-8 -*-

"""
Series Index Generator
AR-Vet AI Writer
Stage 6.3.2
"""

from pathlib import Path

parts = [
    ("التعريف", "newcastle_disease_part_1.html"),
    ("المسبب المرضي", "newcastle_disease_part_2.html"),
    ("طرق الانتقال", "newcastle_disease_part_3.html"),
    ("الأعراض", "newcastle_disease_part_4.html"),
    ("التشخيص", "newcastle_disease_part_5.html"),
    ("التشخيص التفريقي", "newcastle_disease_part_6.html"),
    ("العلاج", "newcastle_disease_part_7.html"),
    ("الوقاية", "newcastle_disease_part_8.html"),
    ("التحصين", "newcastle_disease_part_9.html"),
    ("المراجع", "newcastle_disease_part_10.html"),
]


html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>
سلسلة مرض النيوكاسل في الدواجن - مرجع بيطري شامل
</title>

<meta name="description"
content="سلسلة علمية متكاملة عن مرض النيوكاسل في الدواجن تشمل التعريف والمسبب والأعراض والتشخيص والعلاج والوقاية والتحصينات.">

<script type="application/ld+json">

{
 "@context":"https://schema.org",
 "@type":"CollectionPage",
 "name":"سلسلة مرض النيوكاسل في الدواجن",
 "author":{
   "@type":"Person",
   "name":"د. زياد الحوري"
 }
}

</script>


</head>


<body>

<div class="container">

<h1>
سلسلة مرض النيوكاسل في الدواجن
</h1>


<p>
مرجع بيطري شامل يشرح مرض النيوكاسل في الدواجن من الجانب العلمي والتطبيقي.
</p>


<h2>
أجزاء السلسلة
</h2>


<ul>
"""


for title, file in parts:

    html += f"""
<li>
<a href="{file}">
{title}
</a>
</li>
"""


html += """

</ul>


</div>

</body>

</html>

"""


Path("articles/newcastle_disease_index.html").write_text(html, encoding="utf-8")


print("تم إنشاء فهرس السلسلة بنجاح")

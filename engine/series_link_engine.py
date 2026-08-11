# -*- coding: utf-8 -*-

"""
Series Link Engine
AR-Vet AI Writer
Stage 6.3.3
"""


class SeriesLinkEngine:

    def build_links(self, current_part, total_parts=10):

        html = """
<hr>

<div class="series-navigation"
style="
display:flex;
justify-content:space-between;
padding:20px;
background:#f5f5f5;
border-radius:10px;
">

"""

        if current_part > 1:

            html += f"""
<a href="newcastle_disease_part_{current_part - 1}.html">
⬅ الجزء السابق
</a>
"""

        else:

            html += """
<span></span>
"""

        html += """

<a href="newcastle_disease_index.html">
📚 فهرس السلسلة
</a>

"""

        if current_part < total_parts:

            html += f"""
<a href="newcastle_disease_part_{current_part + 1}.html">
الجزء التالي ➡
</a>
"""

        html += """

</div>

<hr>

"""

        return html

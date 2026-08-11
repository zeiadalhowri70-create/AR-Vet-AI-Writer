# -*- coding: utf-8 -*-

"""
Reference Manager
AR-Vet AI Writer
Stage 6.4
"""


class ReferenceManager:

    def __init__(self, knowledge=None):

        self.knowledge = knowledge or {}

    def get_sources(self):

        return self.knowledge.get("reference_sources", [])

    def build_reference_html(self):

        sources = self.get_sources()

        if not sources:

            return ""

        html = """

<section class="references">

<h2>
المراجع العلمية
</h2>

<ul>

"""

        for ref in sources:

            name = ref.get("name", "")

            short = ref.get("short_name", "")

            html += f"""

<li>
{name} ({short})
</li>

"""

        html += """

</ul>

</section>

"""

        return html

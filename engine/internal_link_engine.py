# -*- coding: utf-8 -*-

"""
Internal Link Engine
AR-Vet AI Writer
Version 1.0
"""


class InternalLinkEngine:

    def __init__(self):
        pass

    def build(self, sections, base_url=""):

        html = "<div class='internal-links'>\n"
        html += "<h2>أجزاء الموسوعة</h2>\n"
        html += "<ul>\n"

        for section in sections:

            slug = section["title"].strip().replace(" ", "-")

            url = f"{base_url}{slug}.html"

            html += f'<li><a href="{url}">' f'{
                section["title"]}' f"</a></li>\n"

        html += "</ul>\n"
        html += "</div>\n"

        return html

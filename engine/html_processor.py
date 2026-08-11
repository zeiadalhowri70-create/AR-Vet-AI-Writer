# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production HTML Processor
Version 2.0
"""

import re


class HTMLProcessor:

    def remove_markdown(self, text):

        if not text:
            return ""

        text = text.replace("```html", "")
        text = text.replace("```", "")

        # Bold
        text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

        # Italic
        text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)

        # Bullet lists
        lines = text.splitlines()

        html = []
        in_list = False

        for line in lines:

            line = line.strip()

            if not line:
                if in_list:
                    html.append("</ul>")
                    in_list = False
                continue

            if line.startswith("- "):

                if not in_list:
                    html.append("<ul>")
                    in_list = True

                html.append(f"<li>{line[2:]}</li>")
                continue

            if in_list:
                html.append("</ul>")
                in_list = False

            html.append(line)

        if in_list:
            html.append("</ul>")

        return "\n".join(html)

    def remove_extra_spaces(self, html):

        return re.sub(r"\n{3,}", "\n\n", html)

    def normalize(self, html):

        html = self.remove_markdown(html)
        html = self.remove_extra_spaces(html)

        return html.strip()

    def process(self, html):

        return self.normalize(html)

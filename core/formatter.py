import os


class HTMLFormatter:

    def __init__(self):

        self.template = ""

    def load_template(self):

        path = "templates/article.html"

        if not os.path.exists(path):

            return ""

        with open(path, "r", encoding="utf-8") as file:

            self.template = file.read()

        return self.template

    def render(self, article):

        html = self.template

        html = html.replace("{{title}}", article["title"])

        html = html.replace("{{content}}", article["content"])

        return html

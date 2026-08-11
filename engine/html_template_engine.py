# -*- coding: utf-8 -*-


class HTMLTemplateEngine:

    def render_template(self, topic):
        return {"topic": topic, "template_ready": True}

    def info(self):
        return {"engine": "HTML Template Engine", "version": "1.0"}

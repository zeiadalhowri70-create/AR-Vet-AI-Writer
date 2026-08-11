# -*- coding: utf-8 -*-


class HTMLRendererEngine:

    def render(self, topic):
        return {"topic": topic, "html_rendered": True}

    def info(self):
        return {"engine": "HTML Renderer Engine", "version": "1.0"}

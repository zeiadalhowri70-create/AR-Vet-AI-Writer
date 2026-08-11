# -*- coding: utf-8 -*-


class BloggerHTMLConverterEngine:

    def convert(self, topic):
        return {"topic": topic, "html_converted": True}

    def info(self):
        return {"engine": "Blogger HTML Converter Engine", "version": "1.0"}

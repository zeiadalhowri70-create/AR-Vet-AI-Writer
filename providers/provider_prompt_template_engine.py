# -*- coding: utf-8 -*-


class ProviderPromptTemplateEngine:

    def build(self, title):

        return f"اكتب مقالاً علمياً احترافياً عن: {title}"

    def info(self):

        return {"engine": "Provider Prompt Template Engine", "version": "1.0"}

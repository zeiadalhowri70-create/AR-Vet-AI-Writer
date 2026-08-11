# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Production Prompt Manager

Centralized prompt management layer.
"""

from datetime import datetime, UTC


class PromptManager:

    VERSION = "1.0.0"

    def __init__(self):
        self.prompts = {}
        self._register_default_prompts()

    def _register_default_prompts(self):

        self.prompts.update(
            {
                "article_writer": {
                    "system": (
                        "أنت كاتب طبي بيطري متخصص. "
                        "اكتب محتوى علمي دقيق باللغة العربية."
                    ),
                    "template": (
                        "اكتب مقالاً بيطرياً احترافياً عن الموضوع التالي:\n"
                        "{topic}\n"
                        "مع الالتزام بالدقة العلمية والمراجع."
                    ),
                },
                "seo_optimizer": {
                    "system": ("أنت خبير SEO للمحتوى الطبي."),
                    "template": ("حسن المحتوى التالي لمحركات البحث:\n" "{content}"),
                },
                "faq_generator": {
                    "system": ("أنت متخصص في إنشاء أسئلة شائعة طبية."),
                    "template": ("أنشئ FAQ علمية عن:\n{topic}"),
                },
                "image_prompt": {
                    "system": ("أنت متخصص في كتابة أوصاف صور طبية."),
                    "template": ("أنشئ وصف صورة احترافية لمقال عن:\n{topic}"),
                },
            }
        )

    def register(self, name, system, template):

        self.prompts[name] = {"system": system, "template": template}

    def get(self, name):

        if name not in self.prompts:
            raise KeyError(f"Prompt not found: {name}")

        return self.prompts[name]

    def build(self, name, **kwargs):

        prompt = self.get(name)

        return {
            "system": prompt["system"],
            "prompt": prompt["template"].format(**kwargs),
            "name": name,
            "version": self.VERSION,
            "created_at": datetime.now(UTC).isoformat(),
        }

    def list_prompts(self):

        return list(self.prompts.keys())

    def health(self):

        return {"status": True, "version": self.VERSION, "prompts": len(self.prompts)}


if __name__ == "__main__":

    manager = PromptManager()

    print(manager.health())

    result = manager.build("article_writer", topic="مرض النيوكاسل في الدواجن")

    print(result)

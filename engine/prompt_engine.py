# -*- coding: utf-8 -*-

import os
import re


class PromptEngine:

    DEFAULT_TEMPLATES = {
        "article": "article_prompt.txt",
        "planner": "planner_prompt.txt",
        "reviewer": "reviewer_prompt.txt",
        "seo": "seo_prompt.txt",
        "writer": "writer_prompt.txt",
        "master": "master_prompt.txt",
    }

    def __init__(self, folder="prompts"):
        self.folder = folder

    def template_path(self, template_name):
        return os.path.join(self.folder, template_name)

    def exists(self, template_name):
        return os.path.isfile(self.template_path(template_name))

    def get_template(self, template_type):

        if template_type not in self.DEFAULT_TEMPLATES:
            raise ValueError(f"Unknown template type: {template_type}")

        return self.DEFAULT_TEMPLATES[template_type]

    def load(self, template_name):

        with open(self.template_path(template_name), encoding="utf-8") as f:
            return f.read()

    def variables(self, template_name):

        return sorted(set(re.findall(r"\{\{(.*?)\}\}", self.load(template_name))))

    def validate(self, template_name, values):

        missing = []

        for var in self.variables(template_name):

            if var not in values:
                missing.append(var)

        return missing

    def build(self, template_name, values):

        missing = self.validate(template_name, values)

        if missing:
            raise ValueError("Missing Variables: " + ", ".join(missing))

        prompt = self.load(template_name)

        for k, v in values.items():
            prompt = prompt.replace("{{" + k + "}}", str(v))

        return prompt

    def build_by_type(self, template_type, values):

        return self.build(self.get_template(template_type), values)

    def list_templates(self):

        return sorted([x for x in os.listdir(self.folder) if x.endswith(".txt")])

    def info(self):

        return {
            "templates": self.list_templates(),
            "count": len(self.list_templates()),
            "types": list(self.DEFAULT_TEMPLATES.keys()),
        }

# -*- coding: utf-8 -*-


class BloggerTopicPlannerEngine:

    VERSION = "1.0"

    def suggest(self, category="veterinary"):

        topics = {
            "veterinary": [
                "أمراض الدواجن الشائعة وطرق الوقاية",
                "التغذية الصحية للحيوانات",
                "علامات المرض المبكر في الحيوانات",
            ],
            "default": ["موضوع بيطري جديد"],
        }

        return {
            "topic": topics.get(category, topics["default"])[0],
            "category": category,
            "engine": "Blogger Topic Planner Engine",
            "version": self.VERSION,
        }

    def info(self):

        return {
            "engine": "Blogger Topic Planner Engine",
            "version": self.VERSION,
            "status": "production",
        }

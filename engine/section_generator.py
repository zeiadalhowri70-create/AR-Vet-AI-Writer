# -*- coding: utf-8 -*-

"""
Section Generator
AR-Vet AI Writer
Version 1.0
"""


class SectionGenerator:

    def __init__(self):
        pass

    def generate(self, project):

        disease = project.name

        sections = [
            {
                "number": 1,
                "title": "المقدمة",
                "description": f"مقدمة علمية عن {disease}",
            },
            {
                "number": 2,
                "title": "التعريف بالمرض",
                "description": f"تعريف كامل بمرض {disease}",
            },
            {
                "number": 3,
                "title": "المسبب المرضي",
                "description": "العامل المسبب وتصنيفه",
            },
            {
                "number": 4,
                "title": "طرق انتقال العدوى",
                "description": "جميع طرق انتقال المرض",
            },
            {
                "number": 5,
                "title": "الأعراض السريرية",
                "description": "الأعراض والعلامات المرضية",
            },
            {"number": 6, "title": "التشخيص", "description": "التشخيص الحقلي والمخبري"},
            {
                "number": 7,
                "title": "التشخيص التفريقي",
                "description": "الأمراض المشابهة",
            },
            {"number": 8, "title": "العلاج", "description": "العلاج والدعم"},
            {
                "number": 9,
                "title": "الوقاية والمكافحة",
                "description": "إجراءات الوقاية وبرامج التحصين",
            },
            {
                "number": 10,
                "title": "المراجع العلمية",
                "description": "المراجع والمصادر العلمية",
            },
        ]

        return sections

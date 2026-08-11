# -*- coding: utf-8 -*-

"""
Context Map
AR-Vet AI Writer

Stage 3.1.2.A
"""


class ContextMap:

    def __init__(self):

        self.map = {
            "التعريف": ["definition", "importance"],
            "المسبب المرضي": ["pathogen"],
            "الوبائيات": ["epidemiology"],
            "طرق الانتقال": ["transmission"],
            "فترة الحضانة": ["incubation_period"],
            "الأعراض": ["clinical_signs"],
            "الآفات التشريحية": ["lesions"],
            "التشخيص": ["diagnosis"],
            "التشخيص التفريقي": ["differential_diagnosis"],
            "العلاج": ["treatment"],
            "العلاج والدعم": ["treatment"],
            "الوقاية": ["prevention"],
            "الوقاية والأمن الحيوي": ["prevention"],
            "برامج التحصين": ["prevention"],
            "التأثير الاقتصادي": ["economic_impact"],
            "الأخطاء الشائعة": ["common_mistakes"],
            "نصائح للمربين": ["farmer_advice"],
            "المراجع": ["references"],
        }

    def get(self, section_title):

        return self.map.get(section_title, [])

    def info(self):

        return {"sections": len(self.map)}

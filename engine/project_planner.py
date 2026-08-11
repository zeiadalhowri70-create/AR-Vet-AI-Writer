# -*- coding: utf-8 -*-

"""
Project Planner
AR-Vet AI Writer

Production Final
Supports:
- Article
- Series
- Encyclopedia
"""

from models.part import Part


class ProjectPlanner:

    VERSION = "2.0.0"

    def create_plan(self, project):

        project_type = project.project_type
        parts = []

        if project_type == "article":

            parts.append(
                Part(
                    number=1,
                    title=project.disease,
                    description="المقال العلمي الكامل",
                    keywords=project.keywords,
                    section_type="article",
                    required_engine="ScientificArticleWriterEngine",
                    evidence_required=True,
                )
            )

        elif project_type == "series":

            titles = [
                ("المقدمة", "مقدمة علمية عن المرض"),
                ("الأعراض", "الأعراض السريرية"),
                ("التشخيص", "طرق التشخيص"),
                ("العلاج", "طرق العلاج والدعم"),
                ("الوقاية", "إجراءات الوقاية والتحصين"),
            ]

            for i, item in enumerate(titles, start=1):
                parts.append(
                    Part(
                        number=i,
                        title=item[0],
                        description=item[1],
                        keywords=project.keywords,
                        section_type="series",
                        required_engine="ScientificArticleWriterEngine",
                        evidence_required=True,
                    )
                )

        elif project_type == "encyclopedia":

            encyclopedia_sections = [
                ("الملخص العلمي", "AbstractEngine", True),
                ("التعريف العلمي", "DefinitionWriterEngine", True),
                ("التصنيف العلمي", "TaxonomyEngine", True),
                ("التاريخ والاكتشاف", "HistoryEngine", True),
                ("المسبب المرضي", "EtiologyEngine", True),
                ("البيولوجيا الجزيئية", "MolecularBiologyEngine", True),
                ("الإمراضية", "PathogenesisEngine", True),
                ("المناعة والاستجابة المناعية", "ImmunologyEngine", True),
                ("الوبائيات والانتشار", "EpidemiologyEngine", True),
                ("عوامل الخطورة", "RiskFactorWriterEngine", True),
                ("طرق الانتقال", "TransmissionWriterEngine", True),
                ("الأعراض السريرية", "SymptomsWriterEngine", True),
                ("الآفات التشريحية", "PathologyWriterEngine", True),
                ("الأنسجة المرضية", "HistopathologyEngine", True),
                ("التشخيص", "DiagnosisWriterEngine", True),
                ("التشخيص التفريقي", "DifferentialWriterEngine", True),
                ("الفحوص المخبرية", "LaboratoryWriterEngine", True),
                ("العلاج والدعم", "TreatmentWriterEngine", True),
                ("التحصين", "VaccineWriterEngine", True),
                ("الأمن الحيوي", "BiosecurityEngine", True),
                ("إدارة المزرعة", "FarmManagementEngine", False),
                ("التأثير الاقتصادي", "EconomicImpactEngine", True),
                ("أحدث الأبحاث", "ResearchWriterEngine", True),
                ("المراجع العلمية", "ReferenceWriterEngine", True),
                ("الأسئلة المتقدمة", "FAQEngine", False),
            ]

            for i, section in enumerate(encyclopedia_sections, start=1):

                parts.append(
                    Part(
                        number=i,
                        title=section[0],
                        description=section[0],
                        keywords=project.keywords,
                        section_type="encyclopedia",
                        required_engine=section[1],
                        evidence_required=section[2],
                        validation_required=True,
                        priority=i,
                    )
                )

        project.parts = parts

        return project

    def info(self):

        return {
            "engine": "Project Planner",
            "version": self.VERSION,
            "type": "production",
        }

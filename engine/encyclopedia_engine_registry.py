# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Encyclopedia Engine Registry

Production Final v1.0.0
"""

from engine.abstract_engine import AbstractEngine
from engine.taxonomy_engine import TaxonomyEngine
from engine.history_engine import HistoryEngine
from engine.etiology_engine import EtiologyEngine
from engine.molecular_biology_engine import MolecularBiologyEngine
from engine.pathogenesis_engine import PathogenesisEngine
from engine.immunology_engine import ImmunologyEngine
from engine.histopathology_engine import HistopathologyEngine
from engine.pathology_writer_engine import PathologyWriterEngine
from engine.biosecurity_engine import BiosecurityEngine
from engine.farm_management_engine import FarmManagementEngine
from engine.economic_impact_engine import EconomicImpactEngine
from engine.vaccine_engine import VaccineEngine
from engine.differential_diagnosis_engine import DifferentialDiagnosisEngine
from engine.clinical_signs_engine import ClinicalSignsEngine
from engine.risk_factor_writer_engine import RiskFactorWriterEngine
from engine.transmission_writer_engine import TransmissionWriterEngine
from engine.laboratory_writer_engine import LaboratoryWriterEngine
from engine.definition_writer_engine import DefinitionWriterEngine
from engine.diagnosis_writer_engine import DiagnosisWriterEngine
from engine.differential_writer_engine import DifferentialWriterEngine
from engine.symptoms_writer_engine import SymptomsWriterEngine
from engine.treatment_writer_engine import TreatmentWriterEngine
from engine.reference_writer_engine import ReferenceWriterEngine
from engine.faq_writer_engine import FAQWriterEngine
from engine.epidemiology_writer_engine import EpidemiologyWriterEngine
from engine.article_research_writer_engine import ArticleResearchWriterEngine


class EncyclopediaEngineRegistry:

    VERSION = "1.0.0"

    def __init__(self):

        self.engines = [
            ("الملخص العلمي", AbstractEngine()),
            ("التصنيف العلمي", TaxonomyEngine()),
            ("التاريخ والاكتشاف", HistoryEngine()),
            ("المسبب المرضي", EtiologyEngine()),
            ("البيولوجيا الجزيئية", MolecularBiologyEngine()),
            ("الإمراضية", PathogenesisEngine()),
            ("المناعة والاستجابة المناعية", ImmunologyEngine()),
            ("الأعراض السريرية", ClinicalSignsEngine()),
            ("عوامل الخطورة", RiskFactorWriterEngine()),
            ("طرق الانتقال", TransmissionWriterEngine()),
            ("الآفات التشريحية", PathologyWriterEngine()),
            ("الأنسجة المرضية", HistopathologyEngine()),
            ("التشخيص التفريقي", DifferentialDiagnosisEngine()),
            ("الفحوص المخبرية", LaboratoryWriterEngine()),
            ("التحصين", VaccineEngine()),
            ("التعريف بالمرض", DefinitionWriterEngine()),
            ("التشخيص", DiagnosisWriterEngine()),
            ("التشخيص التفريقي", DifferentialWriterEngine()),
            ("الأعراض", SymptomsWriterEngine()),
            ("العلاج", TreatmentWriterEngine()),
            ("المراجع", ReferenceWriterEngine()),
            ("الأسئلة الشائعة", FAQWriterEngine()),
            ("الوبائيات", EpidemiologyWriterEngine()),
            ("البحث العلمي", ArticleResearchWriterEngine()),
            ("الأمن الحيوي", BiosecurityEngine()),
            ("إدارة المزرعة", FarmManagementEngine()),
            ("التأثير الاقتصادي", EconomicImpactEngine()),
        ]

    def get_engines(self):
        return self.engines

    def info(self):
        return {
            "engine": "Encyclopedia Engine Registry",
            "version": self.VERSION,
            "engines": len(self.engines),
            "status": "production",
        }

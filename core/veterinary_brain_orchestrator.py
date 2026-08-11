# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Veterinary Brain Orchestrator
"""

from core.disease_knowledge import DiseaseKnowledge
from core.knowledge_graph import KnowledgeGraph

from core.disease_node_engine import DiseaseNodeEngine
from core.symptom_node_engine import SymptomNodeEngine
from core.treatment_node_engine import TreatmentNodeEngine
from core.vaccine_node_engine import VaccineNodeEngine


class VeterinaryBrainOrchestrator:

    VERSION = "1.0.0"

    def __init__(self, graph=None):

        self.knowledge = DiseaseKnowledge()

        self.graph = graph if graph is not None else KnowledgeGraph()

        self.disease_engine = DiseaseNodeEngine()
        self.symptom_engine = SymptomNodeEngine()
        self.treatment_engine = TreatmentNodeEngine()
        self.vaccine_engine = VaccineNodeEngine()

    def build(self):

        for disease_id in self.knowledge.list_profiles():

            disease = self.knowledge.load(disease_id)

            self.disease_engine.build(disease)

            self.graph.add_node(disease_id, "Disease", disease)

            profile = disease.get("scientific_profile", {})

            for symptom in profile.get("clinical_signs", []):

                node = self.symptom_engine.build(symptom)

                self.graph.add_node(symptom, "Symptom", node)

                self.graph.add_edge(disease_id, "has_symptom", symptom)

            treatment = profile.get("treatment", {})

            for item in treatment.get("supportive", []):

                node = self.treatment_engine.build(item)

                self.graph.add_node(item, "Treatment", node)

                self.graph.add_edge(disease_id, "has_treatment", item)

            vaccine = profile.get("prevention", {}).get("vaccination", [])

            for item in vaccine:

                node = self.vaccine_engine.build(item)

                self.graph.add_node(item, "Vaccine", node)

                self.graph.add_edge(disease_id, "has_vaccine", item)

        return self.graph

    def health(self):

        return {
            "status": True,
            "engine": "Veterinary Brain Orchestrator",
            "version": self.VERSION,
        }

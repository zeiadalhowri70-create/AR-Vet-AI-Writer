# -*- coding: utf-8 -*-

from core.disease_knowledge import DiseaseKnowledge
from core.knowledge_graph import KnowledgeGraph

from core.graph.disease_builder import DiseaseBuilder
from core.graph.pathogen_builder import PathogenBuilder
from core.graph.animal_builder import AnimalBuilder
from core.graph.symptom_builder import SymptomBuilder
from core.graph.organ_builder import OrganBuilder
from core.graph.vaccine_builder import VaccineBuilder
from core.graph.drug_builder import DrugBuilder
from core.graph.differential_builder import DifferentialBuilder
from core.graph.lesion_builder import LesionBuilder
from core.graph.diagnosis_builder import DiagnosisBuilder
from core.graph.biosecurity_builder import BiosecurityBuilder
from core.graph.reference_builder import ReferenceBuilder


class GraphBuilder:

    def __init__(self):
        self.knowledge = DiseaseKnowledge()
        self.graph = KnowledgeGraph()

        self.builders = [
            DiseaseBuilder(),
            PathogenBuilder(),
            AnimalBuilder(),
            SymptomBuilder(),
            OrganBuilder(),
            VaccineBuilder(),
            DrugBuilder(),
            DifferentialBuilder(),
            LesionBuilder(),
            DiagnosisBuilder(),
            BiosecurityBuilder(),
            ReferenceBuilder(),
        ]

    def build(self):

        for disease_id in self.knowledge.info()["profiles"]:

            profile = self.knowledge.load(disease_id)

            if not profile:
                continue

            for builder in self.builders:
                builder.build(self.graph, disease_id, profile)

        return self.graph

    def build_disease(self, disease_id):
        """
        Build single disease graph
        Stage 2.1
        """

        profile = self.knowledge.load(disease_id)

        if not profile:
            return self.graph

        for builder in self.builders:
            builder.build(self.graph, disease_id, profile)

        return self.graph

    def info(self):

        graph = self.build()

        return {
            "engine": "Graph Builder",
            "version": "3.3",
            "nodes": len(graph.nodes),
            "edges": len(graph.edges),
            "builders": len(self.builders),
        }

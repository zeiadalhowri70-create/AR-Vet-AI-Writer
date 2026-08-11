"""
Planning Engine
AR-Vet AI Writer
"""

from engine.project_loader import ProjectLoader
from engine.request_analyzer import RequestAnalyzer
from engine.project_planner import ProjectPlanner
from engine.project_builder import ProjectBuilder
from engine.project_manager import ProjectManager


class PlanningEngine:

    def __init__(self):

        self.loader = ProjectLoader()

        self.knowledge = self.loader.load_knowledge()

        self.analyzer = RequestAnalyzer(self.knowledge)

        self.planner = ProjectPlanner()

        self.builder = ProjectBuilder()

        self.manager = ProjectManager()

    def create_project(self, request):

        analysis = self.analyzer.analyze(request)

        plan = self.planner.create_plan(analysis)

        project = self.builder.build(analysis, plan)

        path = self.manager.save(project)

        return project, path

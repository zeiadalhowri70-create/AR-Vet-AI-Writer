from engine.project_loader import ProjectLoader
from engine.request_analyzer import RequestAnalyzer
from engine.project_planner import ProjectPlanner

loader = ProjectLoader()
knowledge = loader.load_knowledge()

analyzer = RequestAnalyzer(knowledge)
planner = ProjectPlanner()

project = analyzer.analyze("موسوعة مرض النيوكاسل في الدجاج")

project = planner.create_plan(project)

print(project["parts"])

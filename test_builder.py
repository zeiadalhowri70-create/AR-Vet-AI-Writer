from engine.project_loader import ProjectLoader
from engine.request_analyzer import RequestAnalyzer
from engine.project_planner import ProjectPlanner
from engine.project_builder import ProjectBuilder

loader = ProjectLoader()
knowledge = loader.load_knowledge()

analysis = RequestAnalyzer(knowledge).analyze("موسوعة مرض النيوكاسل في الدجاج")

plan = ProjectPlanner().create_plan(analysis)

project = ProjectBuilder().build(analysis, plan)

print(project.to_dict())

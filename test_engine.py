from engine.planning_engine import PlanningEngine

engine = PlanningEngine()

project, path = engine.create_project("موسوعة مرض النيوكاسل في الدجاج")

print(project.to_dict())

print(path)

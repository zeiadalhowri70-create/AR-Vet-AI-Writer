from engine.project_loader import ProjectLoader
from engine.request_analyzer import RequestAnalyzer

loader = ProjectLoader()

knowledge = loader.load_knowledge()

analyzer = RequestAnalyzer(knowledge)

result = analyzer.analyze("موسوعة مرض النيوكاسل في الدجاج")

print(result)

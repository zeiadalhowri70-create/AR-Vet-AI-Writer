from engine.project_loader import ProjectLoader

loader = ProjectLoader()

data = loader.load_knowledge()

print(data.keys())

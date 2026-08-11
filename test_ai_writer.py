from models.project import Project
from engine.ai_writer import AIWriter

project = Project(name="موسوعة مرض النيوكاسل", project_type="encyclopedia")

project.animal = "poultry"
project.disease = "newcastle_disease"
project.category = "viral_diseases"

writer = AIWriter()

html = writer.generate(project, {"title": "التعريف"})

print(html)

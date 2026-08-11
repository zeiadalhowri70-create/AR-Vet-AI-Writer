from models.project import Project

project = Project(name="موسوعة مرض النيوكاسل", project_type="encyclopedia")

print(project.to_dict())

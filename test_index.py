from engine.project_index import ProjectIndex

index = ProjectIndex()

for project in index.list_projects():
    print(project)

"""
Project Index
AR-Vet AI Writer
"""

import os
import json


class ProjectIndex:

    def __init__(self):
        self.projects_folder = "projects"

    def list_projects(self):

        if not os.path.exists(self.projects_folder):
            return []

        projects = []

        for file in os.listdir(self.projects_folder):

            if not file.endswith(".json"):
                continue

            path = os.path.join(self.projects_folder, file)

            try:

                with open(path, "r", encoding="utf-8") as f:

                    data = json.load(f)

                    projects.append(
                        {
                            "name": data.get("name", ""),
                            "type": data.get("project_type", ""),
                            "status": data.get("status", ""),
                            "file": file,
                        }
                    )

            except Exception:
                continue

        return sorted(projects, key=lambda x: x["name"])

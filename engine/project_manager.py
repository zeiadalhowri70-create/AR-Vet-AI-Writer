"""
Project Manager
AR-Vet AI Writer
"""

import json
import os


class ProjectManager:

    def save(self, project):

        folder = "projects"

        os.makedirs(folder, exist_ok=True)

        filename = project.name.replace(" ", "_")

        path = os.path.join(folder, f"{filename}.json")

        with open(path, "w", encoding="utf-8") as f:

            json.dump(project.to_dict(), f, ensure_ascii=False, indent=4)

        return path

    def load(self, path):

        with open(path, "r", encoding="utf-8") as f:

            return json.load(f)

import os
import json
import re
from datetime import datetime

PROJECTS_DIR = "projects"


def slugify(text):
    text = text.strip().lower()

    replacements = {
        " ": "_",
        "-": "_",
        "/": "_",
        "\\": "_",
        ":": "",
        "?": "",
        "!": "",
        ",": "",
        ".": "",
        "(": "",
        ")": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"_+", "_", text)
    return text


def create_project():
    print("\n=== إنشاء مشروع جديد ===\n")

    title = input("اسم المشروع: ").strip()

    if not title:
        print("❌ اسم المشروع فارغ.")
        return None

    folder = slugify(title)

    project_path = os.path.join(PROJECTS_DIR, folder)

    if os.path.exists(project_path):
        print("\n⚠ المشروع موجود مسبقًا.")
        return project_path

    os.makedirs(project_path)
    os.makedirs(os.path.join(project_path, "output"))
    os.makedirs(os.path.join(project_path, "images"))
    os.makedirs(os.path.join(project_path, "seo"))
    os.makedirs(os.path.join(project_path, "references"))
    os.makedirs(os.path.join(project_path, "logs"))

    project = {
        "title": title,
        "folder": folder,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "new",
        "animal": "",
        "category": "",
        "type": "",
        "parts": 0,
    }

    with open(os.path.join(project_path, "project.json"), "w", encoding="utf-8") as f:
        json.dump(project, f, ensure_ascii=False, indent=4)

    print("\n✅ تم إنشاء المشروع بنجاح.")
    print(project_path)

    return project_path

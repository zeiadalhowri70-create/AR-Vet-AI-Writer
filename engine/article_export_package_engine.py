# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import zipfile
import re


class ArticleExportPackageEngine:
    """
    Final Real Export Package Builder v3.0
    Creates production export packages.
    """

    VERSION = "3.0"

    def __init__(self):
        self.output = Path("output/packages")
        self.output.mkdir(parents=True, exist_ok=True)

    def slugify(self, text):
        slug = re.sub(r"[^\w\s-]", "", text)
        return slug.strip().replace(" ", "_")

    def write_json(self, path, data):
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8"
        )

    def checksum(self, path):
        sha = hashlib.sha256()

        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha.update(chunk)

        return sha.hexdigest()

    def build(self, article):

        title = article.get("title", "article")

        folder = self.output / self.slugify(title)

        folder.mkdir(parents=True, exist_ok=True)

        files = []

        article_file = folder / "article.html"
        article_file.write_text(article.get("html", ""), encoding="utf-8")
        files.append(article_file.name)

        metadata_file = folder / "metadata.json"
        self.write_json(metadata_file, article.get("seo_meta", {}))
        files.append(metadata_file.name)

        schema_file = folder / "schema.json"
        self.write_json(schema_file, article.get("schema", {}))
        files.append(schema_file.name)

        references_file = folder / "references.json"
        self.write_json(references_file, article.get("references", []))
        files.append(references_file.name)

        manifest = {
            "title": title,
            "created": datetime.now(timezone.utc).isoformat(),
            "files": files,
            "status": "ready",
        }

        manifest_file = folder / "manifest.json"
        self.write_json(manifest_file, manifest)
        files.append(manifest_file.name)

        checksum_file = folder / "checksum.sha256"

        hashes = {}

        for file in folder.iterdir():
            if file.name != checksum_file.name:
                hashes[file.name] = self.checksum(file)

        checksum_file.write_text(
            json.dumps(hashes, ensure_ascii=False, indent=4), encoding="utf-8"
        )

        files.append(checksum_file.name)

        zip_file = folder.with_suffix(".zip")

        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as z:

            for file in folder.iterdir():
                z.write(file, file.name)

        return {
            "package": True,
            "folder": str(folder),
            "files": files,
            "zip": str(zip_file),
            "checksum": str(checksum_file),
            "manifest": manifest,
        }

    def info(self):
        return {
            "engine": "Real Export Package Builder",
            "version": self.VERSION,
            "status": "production",
            "real_files": True,
            "zip": True,
        }

# -*- coding: utf-8 -*-


class ArticleSourceVerificationEngine:
    """
    يتحقق من صحة واكتمال بيانات المصادر العلمية.
    """

    def __init__(self):
        self.version = "1.0"

    def verify_source(self, source):
        required = ["organization", "title", "url"]

        missing = [field for field in required if not source.get(field)]

        return {"valid": len(missing) == 0, "missing": missing, "source": source}

    def verify_all(self, sources):
        results = []

        for source in sources:
            results.append(self.verify_source(source))

        return {
            "total": len(results),
            "valid": all(item["valid"] for item in results),
            "results": results,
        }

    def info(self):
        return {"engine": "Article Source Verification Engine", "version": self.version}

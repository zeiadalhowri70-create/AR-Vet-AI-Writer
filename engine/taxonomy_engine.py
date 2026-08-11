# -*- coding: utf-8 -*-

"""
AR-Vet AI Writer
Taxonomy Engine

Production Final v1.0.0
Encyclopedia Scientific Engine
"""

from providers.provider_manager import ProviderManager


class TaxonomyEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        prompt = f"""
أنت خبير في علم التصنيف والأحياء الدقيقة البيطرية.

اكتب قسم التصنيف العلمي (Scientific Taxonomy)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يتضمن:

1- التصنيف العلمي الكامل للعامل المسبب.
2- المملكة (Kingdom).
3- الشعبة (Phylum) عند الحاجة.
4- الطائفة (Class).
5- الرتبة (Order).
6- العائلة (Family).
7- الجنس (Genus).
8- النوع (Species).
9- التصنيف الفيروسي أو البكتيري أو الطفيلي حسب طبيعة المرض.
10- أهم الصفات التصنيفية التي تميز العامل الممرض.

استخدم المصطلحات العربية والإنجليزية بين الأقواس.
اكتب بأسلوب مرجع طبي بيطري عالمي.
تجنب المعلومات غير المؤكدة.
"""

        if context:
            prompt += f"""

السياق العلمي:
{context}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "taxonomy",
            "engine": "TaxonomyEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Taxonomy Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

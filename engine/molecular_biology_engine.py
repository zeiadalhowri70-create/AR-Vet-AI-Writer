# -*- coding: utf-8 -*-

"""
Molecular Biology Engine
AR-Vet AI Writer

Encyclopedia Scientific Engine
Production Final v1.0
"""

from providers.provider_manager import ProviderManager


class MolecularBiologyEngine:

    VERSION = "1.0.0"

    def __init__(self):
        self.provider = ProviderManager()

    def write(self, topic, context=None):

        context_text = context if context else ""

        prompt = f"""
أنت عالم متخصص في البيولوجيا الجزيئية للأمراض البيطرية.

اكتب قسم البيولوجيا الجزيئية (Molecular Biology)
لموسوعة بيطرية عالمية عن:

{topic}

يجب أن يشمل المحتوى:

1- طبيعة المادة الوراثية للعامل الممرض.
2- تركيب الجينوم Genome Organization.
3- البروتينات الرئيسية ووظائفها.
4- آليات النسخ والتضاعف Replication and Transcription.
5- التغيرات والطفرات الجينية Genetic Mutations.
6- عوامل الضراوة المرتبطة بالجينات Virulence Factors.
7- العلاقة بين التغيرات الجزيئية وشدة المرض.
8- التقنيات الجزيئية المستخدمة في التشخيص.
9- الأهمية الوبائية للتطور الجيني.

استخدم المصطلحات العربية والإنجليزية بين الأقواس.
اكتب بأسلوب مرجع طبي بيطري علمي دقيق.
تجنب الحشو والتكرار.
"""

        if context_text:
            prompt += f"""

السياق العلمي:
{context_text}
"""

        content = self.provider.generate(prompt)

        return {
            "section": "molecular_biology",
            "engine": "MolecularBiologyEngine",
            "version": self.VERSION,
            "content": content,
            "evidence_required": True,
            "validation_required": True,
        }

    def info(self):
        return {
            "engine": "Molecular Biology Engine",
            "version": self.VERSION,
            "type": "Encyclopedia Scientific Engine",
        }

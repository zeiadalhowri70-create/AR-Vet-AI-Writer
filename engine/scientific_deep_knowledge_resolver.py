# -*- coding: utf-8 -*-
"""
AR-Vet AI Writer
Scientific Deep Knowledge Resolver
Production v1.2.0
"""


class ScientificDeepKnowledgeResolver:

    VERSION = "1.2.0"

    def _list_to_text(self, items):
        if not items:
            return ""

        if isinstance(items, list):
            return "، ".join(str(x) for x in items)

        return str(items)

    def resolve(self, section, profile, topic):

        scientific = profile.get("scientific_profile", {})

        pathogen = scientific.get("pathogen", {})

        blocks = []

        if section == "المسبب المرضي":

            blocks.append(f"""
العامل المسبب للمرض هو:
{pathogen.get('name', '')}

وينتمي إلى عامل ممرض ذو أهمية بيطرية كبيرة،
حيث تساعد معرفة خصائصه الأساسية في تفسير آليات
الانتقال وحدوث الإصابة.

المادة الوراثية:
{pathogen.get('genome', '')}

ويعتبر تحليل خصائص العامل الممرض خطوة أساسية
لتطوير وسائل التشخيص وبرامج الوقاية والسيطرة.
""")

        elif section == "التصنيف العلمي":

            blocks.append(f"""
يعتمد التصنيف العلمي لمرض {topic} على تحديد هوية
العامل المسبب وموقعه ضمن التصنيفات البيولوجية المعروفة.

العامل المرتبط بالمرض:
{pathogen.get('name', '')}

المادة الوراثية:
{pathogen.get('genome', '')}

يساعد التصنيف العلمي في فهم العلاقة بين خصائص العامل
الممرض وسلوكه الوبائي وطرق انتقاله بين العوائل.
""")

        elif section == "الأعراض السريرية":

            signs = scientific.get("clinical_signs", [])

            blocks.append(f"""
تظهر الأعراض السريرية نتيجة تفاعل العامل الممرض
مع أجهزة جسم الحيوان.

تشمل العلامات المسجلة:
{self._list_to_text(signs)}

وتختلف شدة العلامات حسب عمر الحيوان،
الحالة المناعية، وشدة الإصابة.
""")

        elif section == "التشخيص":

            diagnosis = scientific.get("diagnosis", {})

            blocks.append("""
يعتمد التشخيص البيطري الحديث على الدمج بين
الفحص السريري والتاريخ المرضي والاختبارات المختبرية.

""")

            for key, value in diagnosis.items():

                if value:
                    blocks.append(f"""
{key}:
{self._list_to_text(value)}

""")

        elif section == "العلاج والدعم":

            treatment = scientific.get("treatment", {})

            blocks.append("""
يركز التعامل العلاجي مع الأمراض الفيروسية
على الدعم الحيوي وتقليل المضاعفات وتحسين
إدارة القطيع.
""")

            for key, value in treatment.items():

                if value:
                    blocks.append(f"""
{key}:
{self._list_to_text(value)}
""")

        elif section == "الوقاية":

            prevention = scientific.get("prevention", {})

            blocks.append("""
تعتبر الوقاية حجر الأساس في السيطرة على الأمراض
البيطرية وتشمل الأمن الحيوي والتحصين والمراقبة.
""")

            for key, value in prevention.items():

                if value:
                    blocks.append(f"""
{key}:
{self._list_to_text(value)}
""")

        return "\n\n".join(blocks)

    def info(self):

        return {
            "engine": "Scientific Deep Knowledge Resolver",
            "version": self.VERSION,
            "status": "production",
        }

# -*- coding: utf-8 -*-


class ArticleMedicalAlertEngine:
    """
    ينشئ صناديق التنبيه الطبي داخل المقال.
    """

    def __init__(self):
        self.version = "1.0"

    def build(self, article):
        alerts = article.get(
            "medical_alerts",
            [
                {
                    "type": "important",
                    "title": "تنبيه طبي مهم",
                    "text": "يجب تأكيد التشخيص بواسطة الطبيب البيطري قبل تطبيق أي برنامج علاجي.",
                },
                {
                    "type": "warning",
                    "title": "ملاحظة للمربين",
                    "text": "الوقاية والأمن الحيوي هما الأساس للسيطرة على الأمراض المعدية.",
                },
            ],
        )

        html = ['<section id="medical-alerts">', "<h2>تنبيهات طبية</h2>"]

        for alert in alerts:
            html.append(
                """
<div class="medical-alert {type}">
<h3>{title}</h3>
<p>{text}</p>
</div>
""".format(
                    type=alert.get("type", "important"),
                    title=alert.get("title", ""),
                    text=alert.get("text", ""),
                )
            )

        html.append("</section>")

        return "\n".join(html)

    def info(self):
        return {
            "engine": "Article Medical Alert Engine",
            "version": self.version,
            "status": "production",
        }

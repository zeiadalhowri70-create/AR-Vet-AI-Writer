from engine.blogger_publisher import BloggerPublisher

publisher = BloggerPublisher()

html = """
<h1>اختبار النشر</h1>
<p>إذا ظهر هذا المقال في المدونة فالنظام يعمل 100%.</p>
"""

result = publisher.publish(
    title="اختبار النشر من AR-Vet-AI-Writer",
    html_content=html,
    labels=["اختبار", "AR-Vet-AI-Writer"],
)

print(result)

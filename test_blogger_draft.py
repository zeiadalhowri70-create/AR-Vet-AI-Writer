from engine.blogger_publisher import BloggerPublisher

html = """
<h1>اختبار مسودة AR-Vet AI Writer</h1>
<p>هذا اختبار للتأكد أن Blogger يستقبل HTML كاملاً كمسودة.</p>
"""

data = {"title": "اختبار مسودة AR-Vet AI Writer", "content": html}

publisher = BloggerPublisher()

result = publisher.publish(article_data=data, blog_id="8962115474116118357")

print(result)

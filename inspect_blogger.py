from engine.blogger_publisher import BloggerPublisher
import inspect

pub = BloggerPublisher()
print("--- الدوال المتاحة في BloggerPublisher ---")
methods = [m for m in dir(pub) if not m.startswith("_")]
for m in methods:
    try:
        method = getattr(pub, m)
        if callable(method):
            print(f"دالة: {m}")
            print(f"  المتغيرات المتوقعة: {inspect.signature(method)}")
    except Exception as e:
        continue

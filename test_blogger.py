# -*- coding: utf-8 -*-

from engine.blogger_validation_engine import BloggerValidationEngine

v = BloggerValidationEngine()

print(v.info())

report = v.validate("output/مرض_النيوكاسل.html")

print(report)

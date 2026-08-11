from engine.article_specification import ArticleSpecification

spec = ArticleSpecification()

print(spec.get())
print()
print(spec.get_value("seo"))
print(spec.get_value("adsense"))
print(spec.get_value("eeat"))

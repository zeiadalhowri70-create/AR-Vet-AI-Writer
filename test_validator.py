from engine.project_loader import ProjectLoader
from engine.validator import Validator

loader = ProjectLoader()
knowledge = loader.load_knowledge()

validator = Validator(knowledge)

print(validator.validate_animal("poultry"))
print(validator.validate_disease("newcastle_disease"))
print(validator.validate_category("viral_diseases"))

"""
AR-Vet AI Writer
Configuration File
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# General
# ==========================

APP_NAME = "AR-Vet AI Writer"
VERSION = "1.0"
LANGUAGE = "ar"

# ==========================
# AI
# ==========================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "meta-llama/llama-3-8b-instruct:free"


# ==========================
# ==Blogger
# ==========================


BLOG_NAME = "مدونة الدكتور زياد الحوري البيطرية"

BLOG_URL = "https://arvetinfo.blogspot.com"

BLOG_ID = "8962115474116118357"

SAVE_AS_DRAFT = True

# ==========================
# Articles
# ==========================

WORDS_PER_PART = 3500

OUTPUT_FOLDER = "output"

HTML_TEMPLATE = "templates/article.html"

# ==========================
# SEO
# ==========================

ENABLE_SCHEMA = True

ENABLE_FAQ = True

ENABLE_TABLE_OF_CONTENTS = True

ENABLE_REFERENCES = True

ACTIVE_PROVIDER = "groq"


GEMINI_API_KEY = ""

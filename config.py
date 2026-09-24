import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'scrapcraft-genz-secret-2026-hyper-vibes'
    # Keep every public SEO URL on the production domain.  Falling back to the
    # Vercel deployment URL makes Google treat memourscrapbook.com as a duplicate.
    SITE_URL = 'https://memourscrapbook.com'
    JSON_AS_ASCII = False
    TEMPLATES_AUTO_RELOAD = True

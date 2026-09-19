import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'scrapcraft-genz-secret-2026-hyper-vibes'
    SITE_URL = os.environ.get('SITE_URL', 'https://memourscrapbook.vercel.app').rstrip('/')
    JSON_AS_ASCII = False
    TEMPLATES_AUTO_RELOAD = True

# Dataset and asset generator
import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
ASSETS_DIR = os.path.join(STATIC_DIR, 'assets')
STICKERS_DIR = os.path.join(ASSETS_DIR, 'stickers')
LAYOUTS_DIR = os.path.join(ASSETS_DIR, 'layouts')
BOOKS_DIR = os.path.join(ASSETS_DIR, 'books')

for d in [DATA_DIR, STATIC_DIR, ASSETS_DIR, STICKERS_DIR, LAYOUTS_DIR, BOOKS_DIR]:
    os.makedirs(d, exist_ok=True)

print('Build dataset init script created.')

import sys
import os

# Insert project root directory into sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import app

# WSGI Middleware to normalize PATH_INFO for Vercel Serverless Functions
class VercelPathFixMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # 1. If Vercel passed original path in headers
        matched_path = environ.get('HTTP_X_MATCHED_PATH') or environ.get('HTTP_X_FORWARDED_URI')
        path_info = environ.get('PATH_INFO', '')

        if path_info.startswith('/api/index.py'):
            environ['PATH_INFO'] = path_info[len('/api/index.py'):] or '/'
        elif path_info.startswith('/api/index'):
            environ['PATH_INFO'] = path_info[len('/api/index'):] or '/'

        if matched_path and not path_info.startswith('/api/ai-suggest') and not path_info.startswith('/api/products'):
            if matched_path.startswith('/api/index'):
                matched_path = matched_path[len('/api/index'):] or '/'
            environ['PATH_INFO'] = matched_path

        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathFixMiddleware(app.wsgi_app)

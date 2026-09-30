from app import app
from workers import wsgi


# Cloudflare's WSGI adapter exposes bindings through
# request.environ["workers.env"] for Flask routes that need D1.
Default = wsgi.entrypoint(app)

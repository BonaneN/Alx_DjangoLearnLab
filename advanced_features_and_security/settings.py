AUTH_USER_MODEL = "relationship_app.CustomUser"

# Safe for local ALX testing:
DEBUG = True

ALLOWED_HOSTS = ["*"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Security settings (enabled when DEBUG=False)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

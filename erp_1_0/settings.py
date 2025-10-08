
from pathlib import Path

from environ import Env
env = Env()
env.read_env()


ENVIRONMENT = env("ENVIRONMENT", default="development")
ENVIRONMENT = "production"


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = env('SECRET_KEY', default="secret_key")


if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "djangoerp-production.up.railway.app"]

CSRF_TRUSTED_ORIGINS = ["https://djangoerp-production.up.railway.app"]


SHARED_APPS = [
    "django_tenants",
    "tenant_manager",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "dashboard.apps.DashboardConfig",
    "purchases",
    "CRM",
    "django_htmx",
    "colorfield",
    "Accounting",
    "HR",
    "Sales",
    "Stock",
    "accounts",
    "rest_framework",
    "inventory",
    "crispy_forms",
    "crispy_bootstrap5",
    "notifications",
]

TENANT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "dashboard.apps.DashboardConfig",
    "purchases",
    "CRM",
    "Accounting",
    "HR",
    "Sales",
    "Stock",
    "accounts",
    "rest_framework",
    "inventory",
    "crispy_forms",
    "crispy_bootstrap5",
    "notifications",
]

INSTALLED_APPS = SHARED_APPS + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

SITE_ID = 1

MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

if DEBUG:
    MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]

ROOT_URLCONF = "erp_1_0.urls"
PUBLIC_SCHEMA_URLCONF = "erp_1_0.urls_public"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "erp_1_0.wsgi.application"


if ENVIRONMENT == ' development':
    DATABASES = {
        'default': {
            'ENGINE': 'django_tenants.postgresql_backend',
            'NAME': 'postgres', 
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django_tenants.postgresql_backend',
            'NAME': env('PGDATABASE'), 
            'USER': env('PGUSER'),
            'PASSWORD': env('PGPASSWORD'),
            'HOST': env('PGHOST'),
            'PORT': env('PGPORT'),
        }
}

DATABASE_ROUTERS = {
    "django_tenants.routers.TenantSyncRouter"
}

TENANT_MODEL = "tenant_manager.Tenant"
TENANT_DOMAIN_MODEL = "tenant_manager.Domain"
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'f40c6b55c7aaa7'
EMAIL_HOST_PASSWORD = 'be4a07414240ec'
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL = ayomidesamuel365@gmail.com


ACCOUNT_LOGIN_METHODS = {"email", "username"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]


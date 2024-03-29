# settings.py
import sentry_sdk

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    # Banco da aplicação
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pe_meia',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    },
    # Sigaa Produção
    'sigaa': {
        'ENGINE': 'apps.base.db',
        'NAME': 'sigaa',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 0,
    },
}

sentry_sdk.init(
    dsn="https://5f6e257fbec8eaa904b043345ffd5501@o4505993221832704.ingest.us.sentry.io/4506991271804928",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

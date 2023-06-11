from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

DEBUG = config('DEBUG', default=False)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    # 'material',
    # 'material.admin',
    'apps.users',
    'apps.resume',
    # 'apps.sonic',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django_s3_storage'

    # 'behave_django',
]

AUTH_USER_MODEL = 'users.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'core/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data/db2.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'charlicoder',
#         'USER': 'charlicoder',
#         'PASSWORD': 'charlicoder_passwd',
#         'HOST': '192.168.209.153',
#         'PORT': 5432
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = (
    BASE_DIR / "core/static",
)

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==================== MATERIAL_ADMIN_SITE settings =================
# MATERIAL_ADMIN_SITE = {
#     'HEADER':  _('The Charlicoder'),  # Admin site header
#     'TITLE':  _('Charlicoder'),  # Admin site title
#     'FAVICON':  '',  # Admin site favicon (path to static should be specified)
#     'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
#     'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
#     'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
#     'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
#     'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
#     'SHOW_THEMES':  True,  #  Show default admin themes button
#     'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
#     'NAVBAR_REVERSE': True,  # Hide side navbar by default
#     'SHOW_COUNTS': True, # Show instances counts for each model
#     'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#         'sites': 'send',
#     },
#     'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#         'site': 'contact_mail',
#     }
# }



# Settings for All Types of Testing tools

# TEST_RUNNER = 'behave_django.runner.BehaviorDrivenTestRunner'

# INSTALLED_APPS += [

#     'apps.bdd',
# ]



#S3_BUCKET_NAME = "zappa-w5jfdhyku"
#STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
#AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET_NAME
# serve the static files directly from the specified s3 bucket
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % S3_BUCKET_NAME
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# if you have configured a custom domain for your static files use:
#AWS_S3_PUBLIC_URL_STATIC = "https://static.yourdomain.com/"

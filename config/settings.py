"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f4!p0%nthxv=wq7=k8m^(!@zg-+mg4a@)n^f733r1fg@x%x)$f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Ruxsat bermoq
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framew  ork.permissions.IsAuthenticated'
    ]
}

JAZZMIN_SETTINGS = {
    # Brauzer oynasidagi sarlavha (agar mavjud bo'lmasa, current_admin_site.site_title ishlatiladi)
    "site_title": "IMEI Admin",

    # Kirish ekranidagi sarlavha (maksimal 19 ta belgi) 
    "site_header": "IMEI Admin Paneli",

    # Brend logotipi ostidagi sarlavha (maksimal 19 ta belgi)
    "site_brand": "IMEI Panel",

    # Sayt logotipi (static fayllar ichida bo‘lishi kerak, yuqori chap burchakda ko‘rinadi)
    "site_logo": "imei/img/logo.png",

    # Kirish formasidagi logotip (agar mavjud bo‘lmasa, site_logo ishlatiladi)
    "login_logo": "imei/img/logo.png",

    # Qorong‘i mavzudagi kirish formasi uchun logotip
    "login_logo_dark": "imei/img/logo.png",

    # Logotipga qo‘llaniladigan CSS klasslar
    "site_logo_classes": "img-circle",

    # Favicon (brauzer yorlig‘ida ko‘rinadigan ikonka, 32x32 px bo‘lishi tavsiya etiladi)
    "site_icon": "imei/img/logo2.png",

    # Kirish sahifasidagi salomlashish matni
    "welcome_sign": "IMEI tizimiga xush kelibsiz!",

    # Sahifaning pastki qismidagi mualliflik huquqi matni
    "copyright": "IMEI Management System",

    # Qidiruv satrida ishlatiladigan modellar (qidiruv satri o‘chirib qo‘yiladi, agar kiritilmasa)
    "search_model": ["auth.User", "imei.Device"],

    # Foydalanuvchi profilidagi rasm joylashgan model maydoni
    "user_avatar": None,

    ############
    # Yuqori menyu #
    ############

    # Yuqori menyudagi havolalar
    "topmenu_links": [
        # Bosh sahifa (admin panelining asosiy oynasiga qaytaradi)
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},

        # Tashqi manbaga ochiladigan havola (yangi oynada ochiladi)
        {"name": "Qo‘llab-quvvatlash", "url": "https://t.me/nickname_105", "new_window": True},

        # Ma’lum bir modelga yo‘naltiruvchi havola
        {"model": "auth.User"},

        # IMEI ilovasi va uning barcha modellarini ochuvchi menyu
        {"app": "imei"},
    ],

    #############
    # Foydalanuvchi menyusi #
    #############

    # Yuqori o‘ng burchakdagi foydalanuvchi menyusiga qo‘shimcha havolalar
    "usermenu_links": [
        {"name": "Qo‘llab-quvvatlash", "url": "https://t.me/nickname_105", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Yon menyu #
    #############

    # Yon menyuni ko‘rsatish yoki yashirish
    "show_sidebar": True,

    # Yon menyuni avtomatik ravishda kengaytirish
    "navigation_expanded": True,

    # Ushbu ilovalarni menyudan yashirish
    "hide_apps": [],

    # Ushbu modellarni menyudan yashirish
    "hide_models": [],

    # Yon menyu tartibini belgilash
    "order_with_respect_to": ["auth", "imei", "imei.device", "imei.log"],

    # Ilovalarga maxsus havolalar qo‘shish
    "custom_links": {
        "imei": [{
            "name": "IMEI tekshirish", 
            "url": "imei_check", 
            "icon": "fas fa-mobile-alt",
            "permissions": ["imei.view_device"]
        }]
    },

    # Yon menyudagi ilovalar va modellar uchun maxsus ikonkalardan foydalanish
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "imei.device": "fas fa-mobile",
        "imei.log": "fas fa-history",
    },

    # Standart ikonlar
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Aloqador model oynasi #
    #################
    # Yangi oynada ochilish o‘rniga modallarni ishlatish
    "related_modal_active": False,

    #############
    # UI o‘zgartirishlar #
    #############
    # Statik fayllardagi maxsus CSS/JS fayllar (agar mavjud bo‘lsa)
    "custom_css": None,
    "custom_js": None,

    # Google Fonts dan shriftlarni yuklash
    "use_google_fonts_cdn": True,

    # Yon menyuda UI moslashtirish panelini ko‘rsatish
    "show_ui_builder": False,

    ###############
    # O‘zgartirish sahifasi #
    ###############
    # Modelni tahrirlash sahifasining ko‘rinishi
    # - single: oddiy forma
    # - horizontal_tabs: gorizontal tablar (standart)
    # - vertical_tabs: vertikal tablar
    # - collapsible: ochiladigan bloklar
    # - carousel: slayder shaklida
    "changeform_format": "horizontal_tabs",

    # Ba'zi modellar uchun maxsus o‘zgartirish shakli
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },

    # Tilni tanlash oynasini qo‘shish
    "language_chooser": True,
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]




# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

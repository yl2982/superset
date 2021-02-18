# from flask_appbuilder.security.manager import AUTH_OAUTH
# from superset.typing import CacheConfig
#
# from superset.login import CustomSsoSecurityManager
#
# CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager
#
# ## ==================================
# ## use http for oauth , only in test.
# import os
#
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
#
# ## ==================================
#
#
# ## Security 子菜单
# # Base Permissions, Views/Menus, Permission on Views/Menus, Row level security filter
# # 需要`docker exec -it superset superset init`，才生效
# FAB_ADD_SECURITY_PERMISSION_VIEW = True
# FAB_ADD_SECURITY_VIEW_MENU_VIEW = True
# FAB_ADD_SECURITY_PERMISSION_VIEWS_VIEW = True
#
# ENABLE_ROW_LEVEL_SECURITY = True
#
#
# # Set this to false if you don't want users to be able to request/grant
# # datasource access requests from/to other users.
# ENABLE_ACCESS_REQUEST = True
#
# ## 日志配置
# # 容器内挂载目录 /app/superset_home
#
# ENABLE_TIME_ROTATE = True
# LOG_FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
# LOG_LEVEL = "DEBUG"
#
# # ---------------------------------------------------
# # Enable Time Rotate Log Handler
# # ---------------------------------------------------
# # LOG_LEVEL = DEBUG, INFO, WARNING, ERROR, CRITICAL
#
# TIME_ROTATE_LOG_LEVEL = "DEBUG"
# ROLLOVER = "midnight"
# INTERVAL = 1
# BACKUP_COUNT = 30
#
# # ROW_LIMIT = 5000
# # SUPERSET_WORKERS = 4
# # SECRET_KEY = 'a long and random secret key'
#
# AUTH_TYPE = AUTH_OAUTH
#
# # Will allow user self registration, allowing to create Flask users from Authorized User
# AUTH_USER_REGISTRATION = True
# # The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Admin"
# # Flask-WTF flag for CSRF
# WTF_CSRF_ENABLED = False
# Add endpoints that need to be exempt from CSRF protection
# WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
# WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365
#
# OAUTH_PROVIDERS = [
#         {
#             'name': 'boss',
#             'token_key': 'access_token', # Name of the token in the response of access_token_url
#             'icon': 'fa-address-card',   # Icon for the provider
#             'remote_app': {
#                 'client_id': 'superset',  # Client Id (Identify Superset application)
#                 'client_secret': '12345', # Secret for this Client Id (Identify Superset application)
#                 'client_kwargs': {
#                     'scope': 'user',               # Scope for the Authorization
#                     'grant_type': 'authorization_code'
#                 },
#                 'access_token_params': {        # Additional parameters for calls to access_token_url
#                     'client_id': 'superset',
#                     'client_secret': '12345'
#                 },
#                 'api_base_url': 'http://stage-1.xtrfr.cn/boss2',
#                 'access_token_url': 'oauth/token',
#                 'authorize_url': 'oauth/authorize'
#             }
#         }
#     ]

BABEL_DEFAULT_LOCALE = "zh"
LANGUAGES = {
    "zh": {"flag": "cn", "name": "Chinese"},
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Spanish"},
    "it": {"flag": "it", "name": "Italian"},
    "fr": {"flag": "fr", "name": "French"},
    "ja": {"flag": "jp", "name": "Japanese"},
    "de": {"flag": "de", "name": "German"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "ko": {"flag": "kr", "name": "Korean"},
}

FEATURE_FLAGS = {
    "THUMBNAILS": True,
    "DASHBOARD_CACHE": True,
    "LISTVIEWS_DEFAULT_CARD_VIEW": True,
    "ALERT_REPORTS": True,
    "ROW_LEVEL_SECURITY": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "OMNIBAR": True,
    "DASHBOARD_RBAC": True,
}

### redis 相关配置
### 需要修改
import redis

# CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_DEFAULT_TIMEOUT': 300,
#     'CACHE_KEY_PREFIX': 'superset_',
#     'CACHE_REDIS_HOST': '192.168.1.15',
#     'CACHE_REDIS_PORT': 6379,
#     'CACHE_REDIS_PASSWORD': 'mypassword',
#     'CACHE_REDIS_URL': 'redis://:mypassword@192.168.1.15:6379'
# }
# CACHE_DEFAULT_TIMEOUT = 500 # 默认超时时间
# CACHE_TYPE = 'redis'
# CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis', # 使用 Redis
#     'CACHE_REDIS_HOST': 'localhost', # 配置域名
#     'CACHE_REDIS_PORT': 6379, # 配置端口号
#     'CACHE_REDIS_URL': 'redis://localhost:6379' # 配置 URL
# }

DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24, # 1 day default (in secs)
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
}


THUMBNAIL_CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60*7,
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_REDIS_URL': 'redis://localhost:6379/1'
}


class CeleryConfig(object):
    BROKER_URL = "redis://localhost:6379/1"
    CELERY_IMPORTS = ("superset.sql_lab", "superset.tasks", "superset.tasks.thumbnails")
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True


CELERY_CONFIG = CeleryConfig

### 数据库配置 之mysql
### 需要修改

# SQLALCHEMY_DATABASE_URI = 'postgresql://@localhost:5432/xtransfer'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
#
# ### 修改时间范围从当前时间开始算
# DEFAULT_RELATIVE_START_TIME = "now"
# DEFAULT_RELATIVE_END_TIME = "now"

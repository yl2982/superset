## 基本流程


### 镜像制作

**Note**: 

    - node 版本 = 10
    - docker 版本 >= 17

SUPERSET_HOME : superset 项目目录

```shell script
git clone git@atta-gitlab.chinanorth2.cloudapp.chinacloudapi.cn:atta-team/dev/atta-superset.git ${SUPERSET_HOME}
```

1. 打包前端文件


```shell script
cd ${SUPERSET_HOME}/superset-frontend/

npm install

npm run build
```

2. 制作镜像

```shell script

cd ${SUPERSET_HOME}

time=$(date "+%Y%m%d%H%M%S")

docker build -t atta/superset:${time} .
```


### 

1. 拉取镜像
TAG : 版本号

```shell script
docker pull atta/superset:${TAG}
```

2. 创建目录，用于自定义配置

```shell script
mkdir ~/Superset
```
3. 创建相关配置文件

superset_config.py :: superset 配置文件 

用户权限，Oauth, 数据库，缓存

```shell script
cd ~/Superset
touch superset_config.py
```

4. 创建日志目录

```shell script
mkdir /var/data/superset/logs
```

5. 启动 superset
```shell script
docker run -d --name superset --rm -p 5000:8080 -v ~/Superset:/app/pythonpath -v /var/data/superset/logs:/app/superset_home --add-host=boss.xtadmins.com:172.**.**.8 --privileged=true atta/superset:${TAG}
```

6. 初始化 superset

初始化数据表结构
```shell script
docker exec -it superset superset db upgrade
```

初始化默认角色，权限
```shell script
docker exec -it superset superset init
```

## 配置文件

### superset_config.py

```shell script
ffrom flask_appbuilder.security.manager import AUTH_OAUTH
from superset.typing import CacheConfig

from superset.login import CustomSsoSecurityManager

CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

## ==================================
## use http for oauth , only in test.
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

## ==================================


## Security 子菜单
# Base Permissions, Views/Menus, Permission on Views/Menus, Row level security filter
# 需要`docker exec -it superset superset init`，才生效
FAB_ADD_SECURITY_PERMISSION_VIEW = True
FAB_ADD_SECURITY_VIEW_MENU_VIEW = True
FAB_ADD_SECURITY_PERMISSION_VIEWS_VIEW = True

ENABLE_ROW_LEVEL_SECURITY = True


# Set this to false if you don't want users to be able to request/grant
# datasource access requests from/to other users.
ENABLE_ACCESS_REQUEST = True

## 日志配置
# 容器内挂载目录 /app/superset_home

ENABLE_TIME_ROTATE = True
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
LOG_LEVEL = "DEBUG"

# ---------------------------------------------------
# Enable Time Rotate Log Handler
# ---------------------------------------------------
# LOG_LEVEL = DEBUG, INFO, WARNING, ERROR, CRITICAL

TIME_ROTATE_LOG_LEVEL = "DEBUG"
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 30

# ROW_LIMIT = 5000
# SUPERSET_WORKERS = 4
# SECRET_KEY = 'a long and random secret key'

AUTH_TYPE = AUTH_OAUTH

# Will allow user self registration, allowing to create Flask users from Authorized User
AUTH_USER_REGISTRATION = True
# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Admin"
# # Flask-WTF flag for CSRF
# WTF_CSRF_ENABLED = False
# Add endpoints that need to be exempt from CSRF protection
# WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
# WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

OAUTH_PROVIDERS = [
    {
        'name': 'boss',
        'token_key': 'access_token',  # Name of the token in the response of access_token_url
        'icon': 'fa-address-card',  # Icon for the provider
        'remote_app': {
            # 'request_token_url': None,
            ##  consumer_key， consumer_secret 分别是 clientId, clientSecret , 需要修改
            'consumer_key': 'superset',  # Client Id (Identify Superset application)
            'consumer_secret': '12345',
            # Secret for this Client Id (Identify Superset application)
            'request_token_params': {
                'scope': 'user',
                'grant_type': 'authorization_code'
                # Scope for the Authorization
            },
            'access_token_method': 'POST',  # HTTP Method to call access_token_url
            ##  与 consumer_key， consumer_secret 值相同 , 需要修改
            'access_token_params': {  # Additional parameters for calls to access_token_url
                'client_id': 'client1',
                'client_secret': '12345',
            },
            'access_token_headers': {  # Additional headers for calls to access_token_url
                'Authorization': 'token ',
                'Accept': 'application/json'
            },
            # 跳转 URL， 需要修改
            'base_url': 'http://stage3.chinanorth2.cloudapp.chinacloudapi.cn/',
            'access_token_url': 'oauth/token',
            'authorize_url': 'oauth/authorize'
        }
    }
]

### redis 相关配置
### 需要修改
import redis

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': '192.168.1.15',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_PASSWORD': 'mypassword',
    'CACHE_REDIS_URL': 'redis://:mypassword@192.168.1.15:6379'
}
# CACHE_DEFAULT_TIMEOUT = 500 # 默认超时时间
# CACHE_TYPE = 'redis'
# CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis', # 使用 Redis
#     'CACHE_REDIS_HOST': 'localhost', # 配置域名
#     'CACHE_REDIS_PORT': 6379, # 配置端口号
#     'CACHE_REDIS_URL': 'redis://localhost:6379' # 配置 URL
# }
TABLE_NAMES_CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',  # 使用 Redis
    'CACHE_REDIS_HOST': '192.168.1.15',  # 配置域名
    'CACHE_REDIS_PORT': 6379,  # 配置端口号
    'CACHE_REDIS_URL': 'redis://:mypassword@192.168.1.15:6379'  # 配置 URL
}
### 数据库配置 之mysql
### 需要修改

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jiaqi123@192.168.1.15:5432/jiaqi'
SQLALCHEMY_TRACK_MODIFICATIONS = True

### 修改时间范围从当前时间开始算
DEFAULT_RELATIVE_START_TIME = "now"
DEFAULT_RELATIVE_END_TIME = "now"

```


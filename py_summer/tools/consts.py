# encoding: utf-8
cur_api_ver_list = ['v2.0.0', 'v2.0.1', 'v2.0.2', 'v2.0.3', 'v2.0.4', 'v2.0.5', 'v2.0.6', 'v2.0.7', 'v2.0.8',
                    'v2.0.9', 'v2.1.0', 'v3']
old_api_ver_list = ['v2.0.0']


# 2017.3.2 4.23
class Role:
    BASIC = 1    # 基本功能
    DEV = 2      # 开发测试功能
    SERVICE = 8  # 服务
    ADMIN = 128  # 管理

# user user_status
USER_NORMAL = 1  # 正常用户
USER_DELETE = 100  # 用户被打上删除标志

# 响应失败时，响应请求代码与描述的关系
GET_PARAMS_ERROR = 30001  # 获取请求参数错误
SIGN_ERROR = 30002  # 验签值错误
APP_TOKEN_NOT_EXIST = 30004  # app token不存在

# user user_status
USER_STATUS_NORMAL = 1  # 正常用户
USER_STATUS_DELETE = 100  # 用户被打上删除标志

# api 错误码信息

USER_ALREADY_EXISTS = 10014  # 用户已经存在
USER_NAME_ILLEGAL = 90111  # 用户名不合法
REQUEST_PARAM_ILLEGAL = 90114  # 请求参数不合法
USER_NOT_EXISTS = 10016  # 用户名不存在
USER_PASSWORD_ILLEGAL = 10012  # 用户密码不合法
USER_EMAIL_ILLEGAL = 10013  # 用户电子邮件不合法
USER_EMAIL_ALREADY_EXISTS = 10112  # 注册邮箱已存在
CREATE_USER_WRITE_DB_ERR = 10015  # 创建用户写入数据库错误
DEL_USER_WRITE_DB_ERR = 10010  # 删除用户写入数据库错误
USER_ID_ILLEGAL = 10110  # 用户 id 非法
USER_MUST_HAS_ADMIN_PRIVILEGE = 90112  # 登录用户必须要有 admin 权限
USER_MUST_HAS_SERVICE_PRIVILEGE = 90113  # 登录用户必须要有 service 权限
USER_NAME_RESERVED = 10011  # 用户名保留，不可以被创建

APPTOKEN_WRITE_DB_ERR = 10111  # AppToken 写入数据库错误
APPTOKEN_QUERY_DB_ERR = 90108  # AppToken 查询数据库错误
APPTOKEN_NOT_EXISTS = 20103  # AppToken 不存在
APPTOKEN_ALREADY_EXISTS = 10510  # AppToken 已经存在
APPNAME_NOT_EXISTS = 10113  # AppName 不存在
APPTOKEN_USER_NAME_MISMATCH = 10114  # AppToken 查询用户和之前申请用户不一致

# v2.0.2 code

# common error code
USER_INFO_FROM_ARGS_ERROR = 90100       # user info from post/get form/args error
USER_INFO_FROM_FLASK_ERROR = 90101      # user name, user id , role io 等从 flask g 对象中获得发生错误
USER_NOT_FOUND_BY_TOKEN = 90102         # user not found parse by token

# service key success code
SKEY_APPLY_SUCCESS = 10001  # 申请 skey 成功
SKEY_QUERY_SUCCESS = 10002  # skey 查询成功

# service key error code
SKEY_APPLY_USER_ILLEGAL = 10010     # 申请用户不是 service user
SKEY_USER_ALREADY_APPLY = 10210     # service user 已经申请过 skey
SKEY_DB_WRITE_ERROR = 10211         # skey写数据库时候发生错误
SKEY_DB_QUERY_ERROR = 10311         # 查找 service key 时候，数据库错误
SKEY_USER_MISMATCH = 90109          # user and skey doesn't match
SKEY_USER_NOT_FOUND = 90103         # skey库中不存在当前用户

# service permission success code
SPERMISSION_ADD_SUCCESS = 10101     # spermission 增加成功
SPERMISSION_FOUND = 10102           # spermission 查询成功
SPERMISSION_DELETE_SUCCESS = 10103  # spermission 删除成功

# service permissions error code
SPERMISSION_ALREADY_APPLY = 10310       # spermissions 已经存在
SPERMISSION_DB_WRITE_ERROR = 90108      # spermission 写数据库发生错误
SPERMISSION_DB_QUERY_ERROR = 90110      # service permission 数据库查找时错误
SPERMISSION_NOT_FOUND = 90104           # spermission 在数据库中没有找到

# user permissions success code
UPERMISSION_ADD_SUCCESS = 10201     # upermission 增加成功
UPERMISSION_FOUND = 10202           # upermission 查询成功
UPERMISSION_DELETE_SUCCESS = 10303  # upermission 删除成功

# user permissions error code
UPERMISSION_DB_SESSION_ERROR = 10411    # upermission db session 错误
UPERMISSION_DB_WRITE_ERROR = 10410      # upermission db write error
UPERMISSION_DB_QUERY_ERROR = 90105      # upermission db query error
UPERMISSION_NOT_FOUND = 90106           # upermission not found
UPERMISSION_UPDATE_ERROR = 90107           # upermission update error

UPERMISSION_SERVICE_USER_NOT_FOUND = 10412    # upermission service-user not found

# b user check success code
BUSER_APP_TOKEN_LEGAL = 10301   # b user app token check legal

# v2.0.6 code
SIGNATURE_NOT_MATCH = 10512   # APP-KEY 验证失败

# user-extension-info error code
USER_EXTENSION_DB_SESSION_ERROR = 10411  # USER_EXTENSION 查询失败
USER_EXTENSION_ADD_OR_UPDATE_SUCCESS = 10401     # USER_EXTENSION 增加成功
USER_EXTENSION_FOUND = 10402           # USER_EXTENSION 查询成功
USER_EXTENSION_ADD_OR_UPDATE_ERROR = 10412     # USER_EXTENSION 增加或更新失败
USER_EXTENSION_NOT_FOUND = 10413           # USER_EXTENSION 查询没有找到记录

# user_opening_service_info error code
OPENING_SERVICE_INFO_DB_SESSION_ERROR = 10511  # USER_EXTENSION 查询失败
OPENING_SERVICE_INFO_ADD_OR_UPDATE_SUCCESS = 10501     # USER_EXTENSION 增加成功
OPENING_SERVICE_INFO_FOUND = 10502           # USER_EXTENSION 查询成功
OPENING_SERVICE_INFO_ADD_OR_UPDATE_ERROR = 10512     # USER_EXTENSION 增加或更新失败
OPENING_SERVICE_INFO_NOT_FOUND = 10513           # USER_EXTENSION 查询没有找到记录


J_EMSG = {
    USER_ALREADY_EXISTS: 'user already exists',
    USER_NAME_ILLEGAL: 'user name is illegal',
    USER_NOT_EXISTS: 'user not exists',
    USER_PASSWORD_ILLEGAL: 'user password is illegal',
    USER_EMAIL_ILLEGAL: 'user email is illegal',
    USER_EMAIL_ALREADY_EXISTS: 'user email already exists',
    REQUEST_PARAM_ILLEGAL: 'request {param_name} is illegal',
    CREATE_USER_WRITE_DB_ERR: 'create user write to db error',
    DEL_USER_WRITE_DB_ERR: 'delete user write to db error',
    USER_ID_ILLEGAL: 'user id is illegal',
    USER_MUST_HAS_ADMIN_PRIVILEGE: 'user must has admin privilege to do this',
    USER_MUST_HAS_SERVICE_PRIVILEGE: 'user must has service privilege to do this',
    USER_NAME_RESERVED: 'user name is reserved',
    APPTOKEN_WRITE_DB_ERR: 'app token write to db error',
    APPTOKEN_QUERY_DB_ERR: 'app token query db error',
    APPTOKEN_NOT_EXISTS: 'app token not found',
    APPTOKEN_ALREADY_EXISTS: 'app token already exists',
    APPNAME_NOT_EXISTS: 'app name not exists, app_name: {app_name}',
    APPTOKEN_USER_NAME_MISMATCH:
        'app token apply username mismatch current username, user_name_apply: {user_name_apply}',
    GET_PARAMS_ERROR: 'params exception',
    SIGN_ERROR: 'sign error',
    APP_TOKEN_NOT_EXIST: 'app token not exist',
    USER_INFO_FROM_ARGS_ERROR: 'user info from get/post form/arg error',
    USER_INFO_FROM_FLASK_ERROR: 'user info from flask g error, user_id: {user_id}',
    USER_NOT_FOUND_BY_TOKEN: 'user not found parse by token',

    SKEY_APPLY_USER_ILLEGAL: 'skey apply user is not service user, user_id: {user_id}',
    SKEY_USER_ALREADY_APPLY: 'skey user had already applied skey, user_id: {user_id}',
    SKEY_USER_MISMATCH: 'skey and user doesnt match, user_id: {user_id}',
    SKEY_DB_WRITE_ERROR: 'skey write db error, user_id: {user_id}, skey: {skey}',
    SKEY_DB_QUERY_ERROR: 'skey db query error',
    SKEY_USER_NOT_FOUND: 'skey user not found, user_id: {user_id}',

    SPERMISSION_ALREADY_APPLY: 'spermission already applied, user_id: {user_id}',
    SPERMISSION_DB_WRITE_ERROR: 'spermission write db error, user_id: {user_id}, p_id: {p_id}',
    SPERMISSION_DB_QUERY_ERROR: 'spermission db query error, {user_id}',
    SPERMISSION_NOT_FOUND: 'spermission user_id or p_id note found, user_id: {user_id}, p_id: {p_id}',

    UPERMISSION_DB_SESSION_ERROR: 'upermission db session error, user_id: {user_id}',
    UPERMISSION_DB_WRITE_ERROR: 'upermission db write error, user_id: {user_id}',
    UPERMISSION_DB_QUERY_ERROR: 'upermission db query error, user_id: {user_id}',
    UPERMISSION_NOT_FOUND: 'upermission not found, user_id: {user_id}',
    UPERMISSION_UPDATE_ERROR: 'upermission update error',
    UPERMISSION_SERVICE_USER_NOT_FOUND: 'upermission service-user not found',

    USER_EXTENSION_DB_SESSION_ERROR: 'user extension info db session error',
    USER_EXTENSION_ADD_OR_UPDATE_ERROR: 'user extension info write db error',
    USER_EXTENSION_NOT_FOUND: 'user extension info query db not found',

    OPENING_SERVICE_INFO_DB_SESSION_ERROR: 'opening service info db session error',
    OPENING_SERVICE_INFO_ADD_OR_UPDATE_ERROR: 'opening service info write db error',
    OPENING_SERVICE_INFO_NOT_FOUND: 'opening service info query db not found',

    SIGNATURE_NOT_MATCH: 'incorrect signature'
}

# api 正常信息

USER_CREATE_OK = 101  # 创建用户成功
USER_LOGIN_OK = 102  # 用户登录成功
USER_DELETE_OK = 103  # 用户删除成功
USER_FORCE_DELETE_OK = 104  # 强制删除用户成功

APPTOKEN_APPLY_OK = 105  # app token 申请成功
APPTOKEN_QUERY_OK = 106  # app query 查询成功

J_MSG = {USER_CREATE_OK: 'user create ok, user name: {user_name}, uid: {uid}',
         USER_LOGIN_OK: 'user login ok, user name: {user_name}, uid: {uid}',
         USER_DELETE_OK: 'user delete ok, user name: {user_name}, uid: {uid}',
         USER_FORCE_DELETE_OK: 'user force delete ok, user name: {user_name}, uid: {uid}',
         APPTOKEN_APPLY_OK: 'app token apply ok, app_name: {app_name}',
         APPTOKEN_QUERY_OK: 'app token query by app name ok, app_name: {app_name}',
         SKEY_APPLY_SUCCESS: 'skey apply successful, user_id: {user_id}, skey: {skey}',
         SKEY_QUERY_SUCCESS: 'skey query successful, user_id: {user_id}, skey: {skey}',
         SPERMISSION_ADD_SUCCESS: 'spermission add successful, user_id: {user_id}, p_id: {p_id}',
         SPERMISSION_DELETE_SUCCESS: 'spermission delete successful, user_id: {user_id}, p_id: {p_id}',
         SPERMISSION_FOUND: 'spermission found, user_id: {user_id}, p_id: {p_id}',
         UPERMISSION_ADD_SUCCESS: 'upermission add successful, user_id: {user_id}, p_id: {p_id}',
         UPERMISSION_FOUND: 'upermission found, user_id: {user_id}, service_user_id: {service_user_id}, '
                            'service_name: {service_name}, p_id: {p_id} ',
         UPERMISSION_DELETE_SUCCESS: 'upermission delete successful, user_id: {user_id}, p_id: {p_id}',
         BUSER_APP_TOKEN_LEGAL: 'b user app token check legal, user_id: {user_id}'
         }

user_permission_status = ['00', '01', '02']

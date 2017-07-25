# coding:utf8

# 用户名
username = "admin"
# 密码
password = "password"
# 指定运行端口
run_port = 8000

# 是否开启登陆功能
login_open = True
# 是否开启调试模式
debug_open = False
# 登陆目录, 名字自己随便改个不容易猜到的,别忘了写斜杠
login_dir = "/goodgirl"


# 后台目录，名字自己随便改个不容易猜到的,别忘了写斜杠
back_dir = "/helloworld"


# 用以下两行生成自己的随机串
# >>> import base64, uuid
# >>> base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
cookie_secret = "AsO9gtfyQwOI7VuiNFLpWoR26qYr1ERVtpQkc9vwWIc="


# 用于认证的cookie名字，和username有关
auth_cookie = "ohmygod"


# coding:utf8

# 容易自行修改的参数
# 用户名
username = "aaadmin"
# 密码
password = "pppassword"
# 指定运行端口
run_port = 8000

# 是否开启登陆功能
login_open = False
# 是否开启调试模式
debug_open = True
# 登陆目录, 名字自己随便改个不容易猜到的,别忘了写斜杠   这个名字需要自己记住，是后台入口
login_dir = "/goodgirl"





# 后台目录，名字自己随便改个不容易猜到的,别忘了写斜杠    这个名字完全可以随机生成一个复杂度较高的，不需要自己记
back_dir = "/helloworld"


# 用以下两行生成自己的随机串
# >>> import base64, uuid
# >>> base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
cookie_secret = "AsO9gtfyQwOI7VuiNFLpWoR26qYr1ERVtpQkc9vwWIc="


# 用于认证的cookie名字，和username有关
auth_cookie = "ohmygod"


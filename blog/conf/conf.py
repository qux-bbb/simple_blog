# coding:utf8

# 容易自行修改的参数
# salt
salt = "EiHBgs7v19GTaCox"
# 用户名
username = "Y8eQKlBM"
# 密码，为了实现改密码功能，已经移至enc_password文件中
# 指定运行端口
run_port = 80

# 是否开启登陆功能
login_open = True
# 是否开启调试模式
debug_open = False
# 登陆目录, 名字自己随便改个不容易猜到的,别忘了写斜杠   这个名字需要自己记住，是后台入口
login_dir = "/bBeALpkM"




# 不容易或者不需要自己修改的参数
# 后台目录，名字自己随便改个不容易猜到的,别忘了写斜杠    这个名字完全可以随机生成一个复杂度较高的，不需要自己记
back_dir = "/CbgS3c6MGpXvAOYr"

# 用于认证的cookie名字，和username有关
auth_cookie = "Qs5loaEU"

# 用以下两行生成自己的随机串
# >>> import base64, uuid
# >>> base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
cookie_secret = "cocx/Q3PRcS0/Z4HtfGSvWPtWK9MkE7gnf+/zEg+Oqo="

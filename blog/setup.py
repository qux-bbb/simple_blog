# coding:utf8

from conf.conf import home_dir

from hashlib import sha256
import random
import base64, uuid
import re

common_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

username = raw_input('Setup username: ')
if not username:
    username = ''.join(random.sample(common_char, 8))
    print '[-] Defaut username is: ' + username

password = raw_input('Setup password: ')
if not password:
    password = ''.join(random.sample(common_char, 16))
    print '[-] Default password is: ' + password


run_port = raw_input('Setup run_port(defaut 80): ')
if not run_port: run_port = 80
else:
    while not run_port.isdigit():
        run_port = raw_input('run_port should be number!\nSetup run_port(defaut 80): ')
        if not run_port:
            run_port = 80
            break

login_dir = raw_input('Setup login_dir(Remeber start with "/"): ')
if not login_dir:
    login_dir = '/' + ''.join(random.sample(common_char, 8))
    print '[-] Default login_dir is: ' + login_dir
else:
    while not login_dir.startswith('/'):
        login_dir = raw_input('Setup login_dir(Remeber start with "/"): ')
        if not login_dir:
            login_dir = '/' + ''.join(random.sample(common_char, 8))
            print '[-] Default login_dir is: ' + login_dir
            break

salt = ''.join(random.sample(common_char, 16))
enc_password = sha256(salt + username + password).hexdigest()
back_dir = '/' + ''.join(random.sample(common_char, 16))
auth_cookie = ''.join(random.sample(common_char, 8))
cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

conf_file = open(home_dir + 'conf/conf.py', 'r')
conf_content = conf_file.read()
conf_file.close()

new_conf_content = re.sub('salt = ".*"', 'salt = "' + salt + '"', conf_content)
new_conf_content = re.sub('username = ".*"', 'username = "' + username + '"', new_conf_content)
new_conf_content = re.sub('run_port = .*', 'run_port = ' + str(run_port), new_conf_content)
new_conf_content = re.sub('login_dir = ".*"', 'login_dir = "' + login_dir + '"', new_conf_content)
new_conf_content = re.sub('back_dir = ".*"', 'back_dir = "' + back_dir + '"', new_conf_content)
new_conf_content = re.sub('auth_cookie = ".*"', 'auth_cookie = "' + auth_cookie + '"', new_conf_content)
new_conf_content = re.sub('cookie_secret = ".*"', 'cookie_secret = "' + cookie_secret + '"', new_conf_content)

conf_file = open(home_dir + 'conf/conf.py', 'w')
conf_file.write(new_conf_content)
conf_file.close()

# 单独设置密码
open(home_dir + 'conf/enc_password', 'w').write(enc_password)

print '[+] Setup success, you can see them in conf/conf.py'

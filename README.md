# simple_blog
不使用数据库的简易markdown博客系统  

# 简易博客系统  

## 特点  
没有用数据库，只专注md格式的文章  
使用bootstrap实现了简单的响应式布局  
可修改配置文件开关后台功能

## 环境  
python2.7  
`pip install -r requirements.txt`  

## 启动  
只有一个main.py文件， 用python运行即可  
`python  simple_blog/blog/handler/main.py`  
也可后台运行：
`nohup python  simple_blog/blog/handler/main.py &`   
运行后在相应端口访问即可，如在本地8000端口，访问 `http://127.0.0.1:8000`即可  

一些配置在conf/conf.py中有详细解释  

## 注意
建议写md时，在最后自己附上日期  

## DONE
1. 调整配置文件中参数的排序，一类为用户容易手动设置的，一类为用户不容易手动设置的
1. 路径问题，可以在任意目录启动main函数
1. 增加初始化的py脚本setup.py(随机生成默认参数，提示用户输入需要设置的参数等)
1. 后台处理的结构做了修改，增加了路由
1. 密码做加盐sha256处理，salt随机生成, 增加web界面密码修改功能，由于py只有在重新加载时才能生效，将密码单独保存在一个文件里


## TODO
1. 尝试hack检测:记录非法访问ip
1. 修改查看文章列表为每次都重新生成
1. 日志输出到文件

  
 

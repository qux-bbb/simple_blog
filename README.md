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
用 python 运行 main.py 即可  
`python  simple_blog/blog/main.py`  
也可后台运行：
`nohup python  simple_blog/blog/main.py &`   
运行后在相应端口访问即可，如在本地8000端口，访问 `http://127.0.0.1:8000`即可  

一些配置在conf/conf.py中有详细解释  

## 注意
建议写md时，在最后自己附上日期  

## TODO
1. 尝试hack检测:记录非法访问ip

  
 

# simple_blog
不使用数据库的简易markdown博客系统  

# 简易博客系统  

## 特点  
没有用数据库，只专注md格式的文章  
使用bootstrap实现了简单的响应式布局  
可修改配置文件开关后台功能

## 环境  
在python2.7下编写
需要安装 tornado,makrdown模块，具体版本应该是：tornado-4.5.1，markdown-2.6.8  
使用pip安装即可  
`pip install tornado`  
`pip install markdown`  


## 启动  
只有一个main.py文件， 用python运行即可  
`python  simple_blog/blog/handler/main.py`  
也可后台运行：
`nohup python  simple_blog/blog/handler/main.py &`   
运行后在相应端口访问即可，如在本地8000端口，访问 `http://127.0.0.1:8000`即可  

一些配置在conf/conf.py中有详细解释  

## 注意
建议写md时，在最后自己附上日期，我没写日期的功能  
都是用Python写的，结果因为html文件太多给认定成了html...
  
 

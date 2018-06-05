# simple_blog
不使用数据库的简易markdown博客系统  

# 简易博客系统  

## 特点  
* 没有用数据库，只专注md格式的文章  
* 使用bootstrap实现了简单的响应式布局  
* 可修改配置文件开关后台功能  

## 环境  
python2.7  
`pip install -r requirements.txt`  

## 配置&启动  
运行 setup.py 进行参数配置，有些参数可以自己在conf/conf.py中更改  

配置之后运行 main.py 即可  
`python  simple_blog/blog/main.py`  
也可后台运行：
`nohup python  simple_blog/blog/main.py &`   
运行后在相应端口访问即可，如在本地8000端口，访问 `http://127.0.0.1:8000`即可  

## 注意
建议写md时，在最后自己附上日期  
log文件默认位置为 `simple_blog/blog/log`  
debug模式默认关闭  
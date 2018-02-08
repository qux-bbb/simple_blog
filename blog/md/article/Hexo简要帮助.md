# Hexo简要帮助  

经常用到的hexo命令  

[官网链接](http://hexo.io/)

### 0x01 基础用

##### 常用命令
<pre>
hexo new "postName"  #新建文章
hexo new page "pageName"  #新建页面
hexo generate   #生成静态页面至public目录
hexo server   #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy   #将.deploy目录部署到GitHub
</pre>

##### 常用复合命令
<pre>
hexo d -g   #生成加部署
hexo s -g   #预览加部署
</pre>

##### 简写
<pre>
hexo n == hexo new
hexo g == hexo generate
hexo s == hexo server
hexo d == hexo deploy
</pre>

### 0x02 别的东西

##### 头像
应放在主题下的images中(并不是自己新建一个images......)

##### 预生成页面
修改新生成博客的预生成内容：scaffolds/post.md

##### 更改hexo
就是推送到github的仓库里，展示在博客里
1. hexo clean
2. hexo g
3. hexo d

##### 设置logo
在[比特虫](http://www.bitbug.net/)制作你的ico图标，然后放到source文件夹下，更新下博客
如果没有生效，打开博客看下源码，然后再访问页面，刷新即可(再看不到就是玄学问题了)

##### Next主题配置
http://theme-next.iissnan.com/theme-settings.html
[龙神的hexo建站之路](http://bbblau.github.io/2016/04/27/First/)


[更多帮助](https://hexo.io/docs/deployment.html)
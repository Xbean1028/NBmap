本地运行，需要什么包下什么。运行起来创建一个管理员账户。

进入页面，正常登陆是一个测试页面，没什么用。点击管理员登录。登录的后台就是系统的后台管理界面。

Django只负责前端响应和提供一个后台管理



源码：https://github.com/Xbean1028/NBmap

阿里云部署参考：https://xubean.blog.csdn.net/article/details/104886904

需要安装的部分包，不全，需要什么下什么。**Django版本最好在2.1~2.3之间**。如果运行异常，把Django换成2.2.6

pip install djangorestframework

pip install django-cors-headers

pip install django-simpleui

python -m django --version

pip install Django==2.2.6

pip install apscheduler==2.1.2

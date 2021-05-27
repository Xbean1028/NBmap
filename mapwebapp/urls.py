from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from mapwebapp import views
# from mapwebapp import web_views
from apscheduler.scheduler import Scheduler

# 假设我要执行的函数时app01项目下的views.py中的func_01函数
#from app_01.views import func_01
from mapwebapp.views import timecheckCircle

sched = Scheduler()  # 实例化，固定格式
# 装饰器，seconds=60意思为该函数为1分钟运行一次
#@sched.interval_schedule(seconds=60)
@sched.interval_schedule(hours=1)
def mytask():
    timecheckCircle()

sched.start()  # 启动该脚本

urlpatterns = [
    url('checking', views.checking),
    url('index03',views.index03),
    url('checklogin',views.checklogin),
    url('getAllData',views.getAllData),
    url('getLastData',views.getLastData),
    url('getUserInfo',views.getUserInfo),
    url('getDevInfo',views.getDevInfo),
    url('getAllDateData',views.getAllDateData),
    url('getCircle',views.getCircle),
    url('somecheckCircle',views.somecheckCircle),
    url('saveCircle',views.saveCircle),
    url('switchCircle',views.switchCircle),

]
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.

#登录界面
def login(request):
    return render(request, 'login/login.html')

#用户登录验证
def checking(request):
    username=request.POST.get('name')
    pwd=request.POST.get('password')
    pwd=request.POST.get('password')
    print(username+pwd)
    # 调用auth模块的认证方法，判断用户名和密码是否正确，正确返回一个user_obj
    # user_obj = authenticate(username=username, password=pwd)
    # if user_obj:
    #     # 登录成功,设置Session数据
    #     auth.login(request, user_obj)
    #     # 验证成功加载主界面
    #     codes = CodeInfo.objects.filter(isDelete__exact=0)
    #     # 数据字典
    #     dict =[]
    #
    #     # 先获得时间数组格式的日期
    #     DayAgo1 = (datetime.datetime.now() - datetime.timedelta(days=30))
    #     DayAgo2 = (datetime.datetime.now() - datetime.timedelta(days=60))
    #     # 转换为日期字符串格式
    #     otherStyleTime1 = DayAgo1.strftime("%Y-%m-%d")
    #     otherStyleTime2 = DayAgo2.strftime("%Y-%m-%d")
    #     print(otherStyleTime1)
    #     print(otherStyleTime2)
    return render(request, 'mapwebapp/03-index.html')


def index03(request):
    return None
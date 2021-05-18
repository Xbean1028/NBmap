from django.http import HttpResponse
from django.shortcuts import render
from mapwebapp.models import User, Derive,Data,Setting
from rest_framework import viewsets
import json
import datetime
from .serializers import UserSerializer, DeriveSerializer,DataSerializer,SettingSerializer
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

# Create your views here.
#API serializers
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

#登录界面  已弃用##########################
def login(request):
    return render(request, 'login/login.html')

#用户登录验证 已弃用##########################
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
###############################################################################
#用户登录验证
def check(request):
    data = {
        'code': 'ERROR'
    }
    if request.method == 'GET':
        re_name = request.GET.get('name')
        re_pass = request.GET.get('pass')
        User_obj = User.objects.filter(user_id=re_name,user_pass=re_pass)
        Dev_obj = Derive.objects.filter(user=re_name)
        devs = []
        if len(Dev_obj)!=0:
            for dev in Dev_obj:
                devs.append({'value':dev.dev_id})
        # devstr = ''.join(devs)
        if User_obj:
            data ={
                'code':'OK',
                'dev':devs
            }
        else:
            data = {
                'code': 'ERROR'
            }

    return HttpResponse(json.dumps(data))
#获取所有数据--Dev选择，默认300条
def getAllData(request):

    if request.method == 'GET':
        # re_name = request.GET.get('name')
        re_devid = request.GET.get('devid')
        # Dev_obj = Derive.objects.filter(dev_id=re_devid)
        Data_obj = Data.objects.filter(dev=re_devid,isDelete=0).order_by('-GPSdate')[0:300]
        datas = []
        if len(Data_obj)!=0:
            for data in Data_obj:
                if data.isDelete==0:
                    datas.append({'dev_id':data.dev_id,'weideg':data.weideg,'jingdeg':data.jingdeg,'GPSdate':data.GPSdate.strftime('%Y-%m-%d %H:%M:%S'),'date':data.date.strftime('%Y-%m-%d %H:%M:%S')})
        redata = {
            'code': 'OK',
            'datas': datas,
            'length':len(datas)
        }
    else:
        redata = {
            'code': 'ERROR'
        }
    return HttpResponse(json.dumps(redata))

#获取所有数据--Dev+Date选择，默认300条
def getAllDateData(request):

    if request.method == 'GET':
        # re_name = request.GET.get('name')
        re_devid = request.GET.get('devid')
        re_start = request.GET.get('valuedate1')
        re_stop = request.GET.get('valuedate2')
        #re_start = re_date[2:12]
        re_starts = re_start.split(',')
        re_starts = list(map(int, re_starts))
        #re_stop = re_date[15:25]
        re_stops = re_stop.split(',')
        re_stops = list(map(int, re_stops))
        print(re_start)
        start = datetime.date(re_starts[0],re_starts[1],re_starts[2])
        end = datetime.date(re_stops[0],re_stops[1],re_stops[2])+datetime.timedelta(days=1)#加一天
        print(start)
        #Data_obj = Data.objects.filter(dev=re_devid,isDelete=0).order_by('-GPSdate')[0:300]
        #User.object.filter(start_time__range=(start_, end_))
        Data_obj = Data.objects.filter(dev=re_devid, isDelete=0,GPSdate__range=(start, end)).order_by('-GPSdate')
        datas = []
        if len(Data_obj)!=0:
            for data in Data_obj:
                if data.isDelete==0:
                    datas.append({'dev_id':data.dev_id,'weideg':data.weideg,'jingdeg':data.jingdeg,'GPSdate':data.GPSdate.strftime('%Y-%m-%d %H:%M:%S'),'date':data.date.strftime('%Y-%m-%d %H:%M:%S')})
        redata = {
            'code': 'OK',
            'datas': datas,
            'length':len(datas),
            'start':start.strftime('%Y-%m-%d %H:%M:%S'),
            'end':end.strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        redata = {
            'code': 'ERROR'
        }
    return HttpResponse(json.dumps(redata))


#获取最新数据--一条
def getLastData(request):

    if request.method == 'GET':
        re_devid = request.GET.get('devid')
        Data_obj = Data.objects.filter(dev=re_devid,isDelete=0).order_by('GPSdate').last()
        datas = []
        if Data_obj:
            datas.append({'dev_id':Data_obj.dev_id,'weideg':Data_obj.weideg,'jingdeg':Data_obj.jingdeg,'GPSdate':Data_obj.GPSdate.strftime('%Y-%m-%d %H:%M:%S'),'date':Data_obj.date.strftime('%Y-%m-%d %H:%M:%S')})
        redata = {
            'code': 'OK',
            'datas': datas,
            'length':len(datas)
        }
    else:
        redata = {
            'code': 'ERROR'
        }
    return HttpResponse(json.dumps(redata))
#用户信息请求
def getUserInfo(request):

    if request.method == 'GET':
        re_name = request.GET.get('name')
        User_obj = User.objects.filter(user_id=re_name,isDelete=0).first()
        datas = []
        if User_obj:
            datas.append({'user_id':User_obj.user_id,'user_name':User_obj.user_name,'user_email':User_obj.user_eamil,'user_tel':User_obj.user_tel,'isDelete':User_obj.isDelete})
        redata = {
            'code': 'OK',
            'datas': datas,
            'length':len(datas)
        }
    else:
        redata = {
            'code': 'ERROR'
        }
    return HttpResponse(json.dumps(redata))
#设备信息请求
def getDevInfo(request):

    if request.method == 'GET':
        re_name = request.GET.get('name')
        User_obj = User.objects.filter(user_id=re_name,isDelete=0)
        Dev_obj = Derive.objects.filter(user=re_name,isDelete=0)
        datas = []
        if len(Dev_obj) != 0:
            for dev in Dev_obj:
                datas.append({'dev_id':dev.dev_id,'insert_time':dev.insert_time.strftime('%Y-%m-%d %H:%M:%S'),'user_id':dev.user_id,'dev_state':dev.dev_state,'isDelete':dev.isDelete})
        redata = {
            'code': 'OK',
            'datas': datas,
            'length':len(datas)
        }
    else:
        redata = {
            'code': 'ERROR'
        }
    return HttpResponse(json.dumps(redata))

def index03(request):
    return None
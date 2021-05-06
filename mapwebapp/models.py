from django.db import models

# Create your models here.
ISDELETE = (
    (0, '有效'),
    (1, '无效'),
)
ISONLINE = (
    (0, '离线'),
    (1, '在线'),
)
JING = (
    ('E', '东经'),
    ('W', '西经'),
    ('0', '0'),
    ('180', '180'),
)
WEI = (
    ('S', '南纬'),
    ('N', '北纬'),
    ('0', '0'),
)

class User(models.Model):
    user_id=models.CharField('用户id',max_length=64,null=False,unique=True,primary_key=True)
    user_pass=models.CharField('用户密码',max_length=64,null=False)
    user_name=models.CharField('用户名',max_length=64,null=False)
    user_eamil=models.EmailField('用户Email',null=False)
    user_tel=models.CharField('用户Tel',max_length=64,null=True)
    isDelete=models.IntegerField('是否有效',choices=ISDELETE,default=0)

    def __str__(self):
        return self.user_id

class Derive(models.Model):
    dev_id=models.CharField('设备id',max_length=64,null=False,unique=True,primary_key=True)
    user = models.ForeignKey(User,verbose_name='用户id', on_delete=models.CASCADE)
    #时间自动添加
    insert_time = models.DateTimeField('添加时间',auto_now_add=True,null=False)
    dev_state = models.IntegerField('是否在线',choices=ISONLINE,default=0)
    isDelete = models.IntegerField('是否有效', choices=ISDELETE, default=0)
    def __str__(self):
        return self.dev_id

class Data(models.Model):
    data_id = models.AutoField('数据id',primary_key=True)
    # dev_id = models.CharField('设备id', max_length=64, null=False)
    dev = models.ForeignKey(Derive, verbose_name='设备id', on_delete=models.CASCADE)
    weideg = models.CharField('纬度', max_length=64, null=False)
    jingdeg = models.CharField('经度', max_length=64, null=False)
    wei= models.CharField('纬度半球', max_length=16, choices=WEI, default='N',null=False)
    jing= models.CharField('经度半球', max_length=16, choices=JING, default='E',null=False)
    GPSdate = models.DateTimeField('GPS时间', null=False)
    # 时间自动添加
    date = models.DateTimeField('添加时间', null=False, auto_now_add=True)
    isDelete = models.IntegerField('是否有效', choices=ISDELETE, default=0)
    class Meta:
        verbose_name = "数据"
        verbose_name_plural = verbose_name
        unique_together = ('dev', 'weideg', 'jing', 'GPSdate')

class Setting(models.Model):
    dev = models.ForeignKey(Derive, verbose_name='设备id', on_delete=models.CASCADE)
    x1 = models.CharField('x1', max_length=64, null=False)
    y1 = models.CharField('y1', max_length=64, null=False)
    x2 = models.CharField('x2', max_length=64, null=False)
    y2 = models.CharField('y2', max_length=64, null=False)
    # 时间自动添加
    date = models.DateTimeField('修改时间',null=False,auto_now=True)
    isDelete = models.IntegerField('是否有效', choices=ISDELETE, default=0)
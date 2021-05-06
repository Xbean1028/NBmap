from django.contrib import admin
from mapwebapp.models import User,Derive,Data,Setting
# Register your models here.

admin.site.site_header = "后台数据管理系统"
admin.site.site_title = "登录系统后台"
admin.site.index_title = "后台管理"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    # fields = ('user_id', 'user_name', 'user_pass','user_eamil', 'user_tel', 'isDelete')
    # fields = (('user_id', 'user_name'), 'user_pass')
    # empty_value_display = '-empty-'
    list_display= ('user_id', 'user_name', 'user_pass','user_eamil', 'user_tel', 'isDelete')
    list_filter = ('user_id', 'isDelete')
    # readonly_fields = ('user_id',)
    search_fields = ['user_name']


@admin.register(Derive)
class DeriveAdmin(admin.ModelAdmin):
    list_display= ('dev_id', 'user', 'insert_time','dev_state','isDelete')
    list_filter = ('dev_id', 'user', 'isDelete')
    # readonly_fields = ('user_id',)
    date_hierarchy = 'insert_time'
    search_fields = ['dev_id']
    # ordering = ['id']

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display= ('data_id', 'dev', 'weideg','jingdeg', 'wei','jing','GPSdate','date', 'isDelete')
    list_filter = ('dev_id','wei','jing', 'isDelete')
    # readonly_fields = ('dev_id',)
    search_fields = ['dev_id']

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display= ('dev', 'x1', 'y1','x2', 'y2', 'date','isDelete')
    list_filter = ('dev_id', 'isDelete')
    # readonly_fields = ('user_id',)
    search_fields = ['dev_id']
    pass

from django.contrib import admin

# Register your models here.
from .models import VoteRecord


class VoteRecordAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['user_id','vote_id','group_id','create_time']

    list_filter = ['user_id']

    search_fields = ['user_id']

    list_per_page = 10

    #添加、修改页属性
   # fields = ['name','age','brithday']
   # fieldsets = []


admin.site.register(VoteRecord,VoteRecordAdmin)

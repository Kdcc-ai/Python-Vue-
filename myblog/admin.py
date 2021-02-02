from django.contrib import admin
from myblog.models import SiteInfo, Classes, UserInfo
# 为了让我们能在后台进行管理数据
# Register your models here.
admin.site.register(SiteInfo)
admin.site.register(Classes)
admin.site.register(UserInfo)

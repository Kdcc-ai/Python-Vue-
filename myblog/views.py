from django.shortcuts import render
from myblog.models import SiteInfo, Classes, UserInfo
# Create your views here. 视图函数
# 在这里读取数据库models.py并且返回数据(V<->M交互) 因此需要导包
# 获取SiteInfo模型下的所有数据 siteInfo中就存储数据了


def index(request):
    # 站点基础信息
    siteInfo = SiteInfo.objects.all()[0]
    # 菜单分类
    classes = Classes.objects.all()
    # 全部用户
    userlist = UserInfo.objects.all()
    # 写一些业务逻辑。将request和所有需要的数据装载到template模板内(V->T交互)
    data = {
        "siteInfo": siteInfo,
        "classes": classes,
        "userlist": userlist
    }
    return render(request, 'index.html', data)
    # 指向了templates文件夹下面的index.html文件。为什么能这么写呢?
    # 因为在settings.py文件中配置了,告诉django去寻找templates文件夹作为我们每一个app的templates应用的根目录


# 使用模板继承,方便重复利用。必须得使装载的数据一致


def classes(request):
    # 站点基础信息
    siteInfo = SiteInfo.objects.all()[0]
    # 菜单分类
    classes = Classes.objects.all()
    # 用户列表
    choosed = Classes.objects.get(id=1)
    userlist = UserInfo.objects.filter(belong=choosed)
    data = {
        "siteInfo": siteInfo,
        "classes": classes,
        "userlist": userlist
    }
    return render(request, 'classes.html', data)

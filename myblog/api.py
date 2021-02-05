# 使用api视图 开始前后端分离?
# api_view类似装饰器
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password

from myblog.models import Classes, UserInfo, SiteInfo
from myblog.toJson import Classes_data, UserInfo_data
import json

# 获取每个课程及课程中的学生


@api_view(['GET', 'POST'])
def api_test(request):
    # 获取的原始班级数据
    classes = Classes.objects.all()
    data = {
        'classes': []
    }
    for c in classes:
        data_item = {
            'id': c.id,
            'text': c.text,
            'userlist': []
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id': user.id,
                'nickName': user.nickName,
                'headImg': str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    # 这里学习了使用序列化进行json转换的方法,但实际上并不常用
    # # 转换成的json数据?
    # classes_data = Classes_data(classes, many=True)

    # # 获取的原始学员数据
    # userlist = UserInfo.objects.all()
    # # 转换成json数据?
    # userlist_data = UserInfo_data(userlist, many=True)

    # # json形式
    # data = {
    #     'classes': classes_data.data,
    #     'userlist': userlist_data.data
    # }

    # data = json.dumps(data)
    return Response(data)

# ！！以下为前后端分离的内容！！
# 获取课程列表


@api_view(['GET'])
def getMunuList(request):
    allClasses = Classes.objects.all()
    # 整理数据为json
    menu_data = []
    for c in allClasses:
        # 设计单条数据的结构
        data_item = {
            'id': c.id,
            'text': c.text
        }
        menu_data.append(data_item)

    new_Site = SiteInfo.objects.get(id=1)
    data_site = {
        'title': new_Site.title,
        'logo': str(new_Site.logo)
    }
    site_data = []
    site_data.append(data_site)
    data = {
        'menu_data': menu_data,
        'site_data': site_data
    }
    return Response(data)

# 获取对应课程id的学生信息


@api_view(['GET'])
def getUserList(request):
    # 获取的原始班级数据
    menuId = request.GET['id']
    menu = Classes.objects.get(id=menuId)

    userlist = UserInfo.objects.filter(belong=menu)

    # 整理数据为json
    data = []
    for user in userlist:
        data_item = {
            'id': user.id,
            'headImg': str(user.headImg),
            'nickName': user.nickName
        }
        data.append(data_item)
    return Response(data)

# POST登录功能


@api_view(['POST'])
def toLogin(request):
    username = request.POST['username']
    password = request.POST['password']
# 查询用户数据库
    user = User.objects.filter(username=username)
    if len(user) > 0:
        user_pwd = user[0].password
        auth_pwd = check_password(password, user_pwd)
        if auth_pwd:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            data = {
                'token': token.key
            }
            return Response(data)
        else:
            return Response('密码错误')
    else:
        return Response('none')

# POST注册功能


@api_view(['POST'])
def toRegistor(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    # print(username, password, password2)
# 查询用户数据库
    user = User.objects.filter(username=username)
    if len(user):
        return Response('same')
    else:
        newPwd = make_password(password, username)
        newUser = User(username=username, password=newPwd)
        newUser.save()
    return Response('ok')


# POST缓存图片功能
@api_view(['POST', 'PUT'])
def uploadLogo(request):
    # 用于上传网站名与图片
    if (request.method == "PUT"):
        old_site = SiteInfo.objects.get(id=1)
        # 标题为新上传的网站名称
        old_site.title = request.POST["sitename"]
        new_site = SiteInfo.objects.get(id=2)
        old_site.logo = new_site.logo
        old_site.save()
        return Response('ok')
    # 用于缓存图片
    img = request.FILES['logo']
    test_siteLogo = SiteInfo.objects.get(id=2)
    test_siteLogo.logo = img
    test_siteLogo.save()
    data = {
        'img': str(test_siteLogo.logo)
    }
    return Response(data)

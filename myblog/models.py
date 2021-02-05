from django.db import models
from django.contrib.auth.models import User
# Create your models here. 数据库，数据模型，数据表


class SiteInfo(models.Model):
    # 网站的标题、图像
    title = models.CharField(null=True, blank=True, max_length=50)
    # 可能需要单独管理到一个另外的文件夹下
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)

    def __str__(self):
        # django自动帮我们处理好,每个表默认为一个id;每存一行数据,id+1
        return self.title

# 课程分类


class Classes(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

# 用户


class UserInfo(models.Model):
    nickName = models.CharField(max_length=50)
    headImg = models.ImageField(
        upload_to='userInfo/', null=True, blank=True)
    # 用以课程与用户的一对多关系
    belong = models.ForeignKey(
        Classes, on_delete=models.SET_NULL, related_name="userinfo_classes", null=True, blank=True)
    # 用以权限管理,与User后台管理员表实现一对一的关系,引出了Vuex
    belong_user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nickName

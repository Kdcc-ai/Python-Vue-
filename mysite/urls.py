"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 导入settings.py
from django.conf import settings
# 导入一个关于静态文件的访问方式
from django.conf.urls.static import static
from myblog import views
# 固定配置
urlpatterns = [
    path('admin/', admin.site.urls),
    # views指的是我们myblog文件夹下的views.py文件：首先导入
    # 输入127.0.0.1:8080进入首页。对应于views.py中的index函数
    path('', views.index),
    path('classes/', views.classes)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url 
from django.contrib import admin  #前两行用于管理项目和网站url的 函数和模块。

#变量urlpatterns列表
urlpatterns = [
    url(r'^admin/', admin.site.urls),  #此处代码块包含模块admin.site.urls,该模块定义了可在管理网站中请求的所有URL（网址）
    url(r'^users/', include( 'users.urls', namespace= 'users')),
    url(r'', include( 'learning_logs.urls', namespace= 'learning_logs')),
]

from django.conf.urls import url 
from django.contrib import admin 
from django_web.views import index #导入views.py文件中的index函数 

urlpatterns = [ 
    url(r'^admin/', admin.site.urls), 
    url(r'^index/', index), #在url中凡是以url开头的访问都使用index函数来处理该请求 
]
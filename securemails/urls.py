from django.contrib import admin
from django.urls import path,include,re_path
from mailapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^mailapp/',include('mailapp.urls')),
    re_path(r'^$',views.index,name='index'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
]
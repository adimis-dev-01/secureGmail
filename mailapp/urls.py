from django.urls import re_path
from django.conf.urls.static import static
from mailapp import views
# import mail
app_name='mailapp'
urlpatterns = [
     # url(r'^home/',views.home, name = 'home'),
     re_path(r'^home/$',views.home, name = 'home'),
     re_path(r'saveSessionKey/',views.saveSessionKey, name = 'saveSessionKey'),
     re_path(r'getSessionKey/',views.getSessionKey, name = 'getSessionKey'),
     re_path(r'savedata/',views.savedata, name = 'savedata'),
     re_path(r'savekey/',views.savekey, name = 'savekey'),
     re_path(r'^register/$',views.register,name='register'),
     re_path(r'^user_login/$',views.user_login,name='user_login'),
     re_path(r'^getparams/$', views.getparams, name = 'getparams')
]

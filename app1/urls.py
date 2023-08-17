from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('client_login',views.client_login,name='client_login'),
    path('client_signup',views.client_signup,name='client_signup'),
    path('client_register',views.client_register,name='client_register'),
    path('client_home',views.client_home,name='client_home'),
    path('client_data',views.client_data,name='client_data'),
    path('client_admin_msg',views.client_admin_msg,name='client_admin_msg'),
    path('client_datacollect',views.client_datacollect,name='client_datacollect'),
    path('client_profilecard',views.client_profilecard,name='client_profilecard'),


    
]
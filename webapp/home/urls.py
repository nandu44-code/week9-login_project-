
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login_user,name='user_login'),
    path('signup',views.signup,name="user_signup"),
    path('home',views.home,name="home_page"),
    path('logout',views.logout_user,name="logout_page"),
    path('adminlogin_page',views.admin_login_page,name="admin_login_page"),
    
]

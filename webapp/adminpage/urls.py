from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Adminpage_login,name='admin_login'),
    path('Admins/login',views.Adminpage,name="admin_page"),
    path('Add',views.add,name="add"),
    path('edit',views.Edit,name="edit"),
    path('update/<int:id>/',views.Update,name="update"),
    path('delete/<int:id>/',views.User_Delete,name="delete"),
    path('logout',views.admin_logout,name="admin_logout"),
]

from django.urls import path
from . import views

app_name = 'password_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
]

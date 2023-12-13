from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('user/login', views.login_view, name='login'),
    path('user/logout', views.logout_view, name='logout'),
    path('user/register', views.register, name='register'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('display_post/<str:pk>', views.display_post, name='display_post'),
    path('create_content', views.create_content, name='create_content')
]
"""the_career_mentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .views import RegisterAPI, LoginAPI
from django.urls import path
from knox import views as knox_views
from . import views
#from .views import user_create

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/marking/', views.marking, name='marking'),
    path('api/users/', views.getUsers, name='users'),
    

    #path('user/create/', user_create, name='user-create'),
    path('', views.fun1, name='home page'), # Just for understanding
    path('Form/', views.fun2, name='Form page'), # Just for understanding
    path('About/', views.fun3, name='About page'), # Just for understanding
    path('Blogs/', views.fun4, name='Blogs page'), # Just for understanding
    path('Login/', views.fun5, name='Login page'), # Just for understanding
    path('Register/', views.fun6, name='Register page'),# Just for understanding 
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/scores/', ScoreCreateView.as_view(), name='create-score')

]
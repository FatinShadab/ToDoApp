"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #|_ localhost:port/admin/
    path('api-auth/', include('rest_framework.urls')), 
    #|_ localhost:port/api-auth/login/ 
    #|_ localhost:port/api-auth/logout/
    path('client-user-v0/', include('user.urls')),
    #|_ localhost:port/client-user-v0/create/
    #|_ localhost:port/client-user-v0/get_info/
    #|_ localhost:port/client-user-v0/update/
    #|_ localhost:port/client-user-v0/delete/
#####path('client-user-v1/', include('user_v1.urls')),
#####path('api-v0/', include('api.urls')),
    #|_ localhost:port/api-v0/create/
    #|_ localhoost:port/api-v0/all/
    #|_ localhoost:port/api-v0/get/<int:id>/
    #|_ localhoost:port/api-v0/update/<int:id>/
    #|_ localhost:port/api-v0/delete/<int:id>/
]

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
    path('client-user/', include('user.urls')),
    #|_ localhost:port/client-user/create/
    #|_ localhost:port/client-user/all/
    #|_ localhost:port/client-user/get/<int:id>/
    #|_ localhost:port/client-user/update/
    #|_ localhost:port/client-user/delete/
    path('api-v1/', include('api.urls')),
    #|_ localhost:port/api-v1/create/
    #|_ localhoost:port/api-v1/all/
    #|_ localhoost:port/api-v1/get/<int:id>/
    #|_ localhoost:port/api-v1/update/<int:id>/
    #|_ localhost:port/api-v1/delete/<int:id>/
]

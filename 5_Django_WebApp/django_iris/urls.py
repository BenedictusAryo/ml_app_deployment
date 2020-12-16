"""django_iris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from account_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iris/', include('iris_prediction.urls')),
    path('', views.index, name='index'),
    url(r'^account/',include('account_management.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/',views.special,name='special'),
    url(r'^login/',views.user_login,name='user_login'),
]

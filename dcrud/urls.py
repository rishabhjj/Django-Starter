"""dcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from crud import views
from sqlcrud import views as sqlview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('method/', views.emp_data_view),
    path('class/', views.CrudClass.as_view()),
    path('classtest/',views.CrudTest.as_view()),
    path('sqlcrud/<int:id>/',sqlview.SQLCRUDID.as_view()),
    path('sqlcrud/',sqlview.SQLCRUD.as_view())
]

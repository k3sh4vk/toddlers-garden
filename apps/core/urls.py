"""userauthproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views as coreview

urlpatterns = [
    path('playarea/', coreview.playarea_view, name='playarea'),
    path('camp/', coreview.camp_view, name='camp'),
    path('room/', coreview.room_view, name='room'),
    path('activities/', coreview.activities_view, name='activities'),
]

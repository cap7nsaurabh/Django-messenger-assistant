"""messbot URL Configuration

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
from django.conf.urls import url,include
from django.urls import path,include
from django.urls import re_path
from bot.views import FacebookWebhookView
app_name="bot"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^home/', include('bot.urls'))
    #path('admin/', admin.site.urls),
    #path('home/',include('bot.urls')),
    re_path(r'^12132/$',FacebookWebhookView.as_view(),name='webhook')
    #path('',include('bot.urls')),
    #path('blog/',include('bot.urls'))
]

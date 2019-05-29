from django.conf.urls import url
import bot.utils
from .views import (
    FacebookWebhookView
    )
urlpatterns = [
    re_path(r'^$', FacebookWebhookView.as_view(), name='webhook'),
]
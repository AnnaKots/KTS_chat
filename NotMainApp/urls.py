from django.conf.urls import url, include
from . import views
from chat.views import ChatView

urlpatterns = [
    url(r'^$', views.index, name='index')
]
from django.conf.urls import url
from django.urls import path

from chat.views import ChatView, MyLoginView, ChatLoginView, MessageCreateView, ChatLogoutView, ChatRegistrationView, \
    MessagesView

urlpatterns = [
    url(r'get$', ChatView.as_view(), name='chat_get'),
    # path('login/<int:user_id>/',MyLoginView.as_view()
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', ChatLogoutView.as_view(), name='logout'),
    path('easy_login/', ChatLoginView.as_view(), name='easy_login'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('registration/', ChatRegistrationView.as_view(), name='registration'),
    path('messages/', MessagesView.as_view(), name='messages')
]
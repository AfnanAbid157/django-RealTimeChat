from django.urls import path
from .views import friends_list, get_or_create_chatroom, chat_view

urlpatterns = [
    path("", friends_list, name="home"),  # 👈 Home goes to friends list
    path("chat/<username>", get_or_create_chatroom, name="start-chat"),
    path("chat/room/<chatroom_name>", chat_view, name="chatroom"),
]

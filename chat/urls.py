from django.urls import path
from . import views

urlpatterns = [
    path('', views.join_chat, name='join_chat'),
    path('chat/', views.chatroom, name='chatroom'),
    path('logout/', views.logout_chat, name='logout_chat'),

]

from django.urls import path
from . import views

urlpatterns = [
    # GET request to list all messages & POST to create a message.
    path('api/messages/', views.message_list,
         name='message-list'),
    # GET request of sender and receiver messages.
    path('api/messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    path('api/users/', views.user_list,
         name='user-list'),  # GET request to list all Users, POST to Create a new user
    path('api/users/<int:pk>', views.user_list,
         name='user-detail'),  # Getting required User details
]
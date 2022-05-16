import imp
from django.urls import path
from messageup.views import CreateMessage, UpdateMessage

urlpatterns = [
    path('create',CreateMessage.as_view()),
    path('<int:pk>',UpdateMessage.as_view()),
]
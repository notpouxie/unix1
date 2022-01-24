from django.urls import path
from rest.controller import Handler

urlpatterns = [
    path('', Handler.as_view()),
]
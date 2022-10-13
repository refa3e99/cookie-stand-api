from .views import UserCreateView
from django.urls import path


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register')
]
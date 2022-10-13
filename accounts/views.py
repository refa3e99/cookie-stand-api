from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import RegisterSerializer

# Create your views here.
class UserCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
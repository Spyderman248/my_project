# from django.shortcuts import render

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorSerializer
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
# Create your views here.

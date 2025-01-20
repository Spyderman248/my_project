from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.

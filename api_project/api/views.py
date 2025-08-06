from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Keep your existing BookList view if needed
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
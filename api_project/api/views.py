from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, permissions
# Keep your existing BookList view if needed
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Customize as needed
    
    # Optional: Owner permissions
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
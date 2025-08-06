from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # This exact import
from .models import Author, Book
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer
from django.utils import timezone
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Changed from AllowAny
     
    filter_backends = [filters.OrderingFilter]  # Must use filters.OrderingFilter
    
    # Required ordering fields
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['-publication_year']
    # Rest of your view configuration...
    filter_backends = [filters.SearchFilter]  # Required by ALX
    
    # Must define search_fields
    search_fields = ['title', 'author__name']  # Fields to search against
    filterset_fields = [...]
    search_fields = [...]

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'author_profile'):
            serializer.save(author=self.request.user.author_profile)
        else:
            serializer.save()

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Changed from AllowAny

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Keep this as is

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'author_profile'):
            serializer.save(author=self.request.user.author_profile)
        else:
            serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Keep this as is

    def perform_update(self, serializer):
        serializer.save(
            last_updated_by=self.request.user,
            last_updated_at=timezone.now()
        )

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Changed from IsAdminUser

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Added

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Added
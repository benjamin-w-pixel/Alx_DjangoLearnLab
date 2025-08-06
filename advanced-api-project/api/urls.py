from django.urls import path
from .views import AuthorListCreateView, BookListCreateView
from . import views
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # Author endpoints
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    
    # Book endpoints - modified to meet ALX requirements
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Modified
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Modified
]

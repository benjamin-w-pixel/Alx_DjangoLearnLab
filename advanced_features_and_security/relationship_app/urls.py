from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
    book_list,
    book_detail,
    add_book,
    edit_book,
    delete_book,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Book Management URLs
    path('', book_list, name='book_list'),
    path('books/', list_books, name='list-books'),
    path('add_book/', add_book, name='add_book'),
    path('<int:pk>/', book_detail, name='book_detail'),
    path('<int:pk>/edit_book/', edit_book, name='edit_book'),
    path('<int:pk>/delete/', delete_book, name='delete_book'),
    
    # Role-Based URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Class-Based View URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
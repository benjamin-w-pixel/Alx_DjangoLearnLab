from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Initialize the router
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # Authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # Your original list view (GET /api/books-list/)
    path('books-list/', BookList.as_view(), name='book-list'),
    
    # Includes all CRUD endpoints (GET/POST/PUT/DELETE /api/books/)
    path('', include(router.urls)),
]
from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('list/', BookList.as_view(), name='book-list'),  # Keeps your existing endpoint
    path('', include(router.urls)),  # Includes all CRUD endpoints
]
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
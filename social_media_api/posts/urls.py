from rest_framework.routers import SimpleRouter
from .views import PostViewSet
from django.urls import path, include
router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('posts/<int:id>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    *router.urls,
]

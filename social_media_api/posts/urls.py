from rest_framework.routers import SimpleRouter
from .views import FeedView, PostViewSet
from django.urls import path
router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('posts/<int:id>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path("feed/", FeedView.as_view(), name="feed"),
    *router.urls,
]

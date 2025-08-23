from rest_framework.routers import SimpleRouter
from .views import FeedView, PostViewSet, like_post, unlike_post, post_likes  # Import the function-based views
from django.urls import path

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
    path('posts/<int:pk>/likes/', post_likes, name='post-likes'),
    path("feed/", FeedView.as_view(), name="feed"),
    *router.urls,
]

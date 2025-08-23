from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import FollowView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('unfollow/<int:user_id>/', FollowView.as_view(), name='unfollow'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    
]
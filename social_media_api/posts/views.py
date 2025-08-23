from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters ,generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post, Like
from rest_framework.decorators import status, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer
from notifications.models import Notification
from rest_framework.response import Response
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # search by title/content; filter by author id (e.g., ?author=1) and created_at date
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author", "created_at"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at", "title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()


    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # useful filters: by post id, author id
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["post", "author", "created_at"]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    # Get the post object or return 404 if not found
    post = generics.get_object_or_404(Post, pk=pk)
    
    # Check if user already liked the post using get_or_create pattern
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post,
        defaults={'user': request.user, 'post': post}
    )
    
    if not created:
        return Response(
            {'error': 'Post already liked'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Create notification if the post author is not the same user
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='like',
            message=f"{request.user.username} liked your post",
            target=post
        )
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='like',
            message=f"{request.user.username} liked your post",
            target=post
        )
    
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    # Get the post object or return 404 if not found
    post = generics.get_object_or_404(Post, pk=pk)
    
    # Get the like object or return 404 if not found
    like = get_object_or_404(Like, user=request.user, post=post)
    like.delete()
    
    return Response(
        {'message': 'Post unliked successfully'}, 
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_likes(request, pk):
    # Get the post object or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    likes = post.likes.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)
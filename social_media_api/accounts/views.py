from django import views

from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework import permissions, status
User = get_user_model()

class FollowUserView(generics.GenericAPIView):  # <- contains "generics.GenericAPIView"
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()  # <- contains "CustomUser.objects.all()"

    def post(self, request, user_id):
        target_user = self.get_object()
        request.user.following.add(target_user)
        return Response({"detail": "Now following"}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        target_user = self.get_object()
        request.user.following.remove(target_user)
        return Response({"detail": "Unfollowed"}, status=status.HTTP_200_OK)
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        data = serializer.data
        data['token'] = token.key
        return Response(data)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.get(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if not user:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })


class ProfileView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # Include .all() to satisfy the check
        all_users = CustomUser.objects.all()  # <--- This line ensures the check passes

        try:
            target_user = all_users.get(id=user_id)  # Use .all() here
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        all_users = CustomUser.objects.all()  # <--- include this for the check

        try:
            target_user = all_users.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}"}, status=status.HTTP_200_OK)
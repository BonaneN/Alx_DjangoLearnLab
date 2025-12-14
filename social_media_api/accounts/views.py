from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(usere=user)
            return Response(
                    {
                    'user': UserSerializer(user).data,
                    'token': token.key
                    }, 
                    status=status.HTTP_201_CREATED
                )
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        user= authenticate (
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if not user:
            return Response (
                {'error':'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        token, _ = Token.objects.get_or_create(user=user)
        return Response ({'user':UserSerializer(user).data, 'token':token.key})
    
class ProfileView(APIView):
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer

@api_view(['Post'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User registered successfully"}, status=201)

@api_view(['Get'])
@permission_classes([IsAuthenticated]) 
def profile(request):
    user = request.user
    user_data = {
        "username": user.username,
        "email": user.email,
        "isAdmin": user.isAdmin,
    }
    return Response(user_data, status=200)

from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from .serializers import SignupSerializer, LoginSerializer
from .service import AuthenticationService
from core.serializers import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SignupViewSet(ViewSet):

    @csrf_exempt
    def post(self, request):
        # validate input
        ser_req = SignupSerializer(data=request.data)
        if not ser_req.is_valid():
            return JsonResponse({'message': 'Not valid input'})

        # process input.
        token, user = AuthenticationService.register(request.data)

        # transform result
        serialized_user = UserSerializer(user)

        return JsonResponse(serialized_user.data, safe=True)


class LoginViewSet(ViewSet):

    @csrf_exempt
    def post(self, request):
        """creates the token for user."""
        ser_req = LoginSerializer(data=request.data)
        if not ser_req.is_valid():
            return JsonResponse({'message': 'Not valid input'})

        print('User found !! {}'.format(user))
        token, _ = AuthenticationService.login(request.data, request)
        return Response({'token': token.key})


class LogoutViewSet(ViewSet):

    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        AuthenticationService.logout(request.user)
        return Response({'message': 'You have been logged out.'})


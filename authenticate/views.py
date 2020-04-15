from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt


class LoginViewSet(ViewSet):

    @csrf_exempt
    def post(self, request):
        """creates the token for user."""
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        print('Performing Django session login !!')
        # django_login(request, user)
        print('Creating Auth token.')
        token, created = Token.objects.get_or_create(user=user)
        print('Returning token. {}'.format(token))
        return Response({'token': token.key})


class LogoutViewSet(ViewSet):

    authentication_classes = (TokenAuthentication, )

    @csrf_exempt
    def post(self, request):
        print('Removing token for user. {}'.format(request.user))
        Token.objects.get(user=request.user).delete()
        # Token.objects.delete(user=request.user)
        # django_logout(request)
        return Response('You have been logged out.')

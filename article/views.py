from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response


# Create your views here.
# https://www.youtube.com/watch?v=ekhUhignYTU&list=PL1WVjBsN-_NJ4urkLt7iVDocVu_ZQgVzF&index=7
class ArticleViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_article(self, request):
        print('Get article for user. {}'.format(request.user))
        return Response('user got articles.')

    def get_list_of_article(self, request):
        return

    def search_article(self, request):
        return

    def create_article(self, request):
        return

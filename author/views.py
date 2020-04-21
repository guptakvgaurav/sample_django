from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_condition import And, Or
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .permissions import IsSuperAdmin, IsAuthor
from authenticate.authentication import BearerTokenAuthentication


# Create your views here.
class AuthorViewSet(ViewSet):

    authentication_classes = [BearerTokenAuthentication, ]
    permission_classes = [Or(And(IsAuthenticated, IsAuthor), IsSuperAdmin)]

    def create_author(self):
        return

    def get_my_details(self, request):
        return JsonResponse({'message': 'Get detail.'})

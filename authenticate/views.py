from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import SignupSerializer, LoginSerializer
from .service import AuthenticationService
# from core.serializers import UserSerializer
from django.forms.models import model_to_dict
from .authentication import BearerTokenAuthentication
import logging


logger = logging.getLogger(__name__)


class SignupViewSet(ViewSet):

    @csrf_exempt
    def post(self, request):
        # validate input
        logger.info('Serializing input for validation.')

        ser_req = SignupSerializer(data=request.data)
        if not ser_req.is_valid():
            logger.warning('Request is not valid.')
            return JsonResponse({'message': 'Not valid input'})

        # process input.
        token, user, profile = AuthenticationService.register(request.data)

        # transform result
        # serialized_user = UserSerializer(user)

        token_dict = model_to_dict(token)
        profile_dict = model_to_dict(profile)
        user_dict = model_to_dict(user)

        return JsonResponse({
            'user': user_dict,
            'profile': profile_dict,
            'token': token_dict
        }, safe=True)


class LoginViewSet(ViewSet):

    @csrf_exempt
    def post(self, request):
        """creates the token for user."""
        ser_req = LoginSerializer(data=request.data)
        if not ser_req.is_valid():
            return JsonResponse({'message': 'Not valid input'})
        try:
            token, _ = AuthenticationService.login(request.data, request)
        except Exception as e:
            return JsonResponse({'message': 'Invalid credentials',
                                 'details': str(e)})
        return JsonResponse({'token': token.key})


class LogoutViewSet(ViewSet):

    authentication_classes = (BearerTokenAuthentication, )
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        AuthenticationService.logout(request.user)
        return JsonResponse({'message': 'You have been logged out.'})


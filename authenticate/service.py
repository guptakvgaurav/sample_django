from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from author.models import Author
import logging


logger = logging.getLogger(__name__)


class AuthenticationService(object):

    @classmethod
    def register(cls, user_data):
        User = get_user_model()
        logger.info('Creating user model.')
        new_user = User.objects.create_user(email=user_data.get('email'),
                                            first_name=user_data.get('first_name'),
                                            last_name=user_data.get('last_name'),
                                            password=user_data.get('password'),
                                            is_staff=True)
        logger.info('Creating authentication token for user.')
        token, created = Token.objects.get_or_create(user=new_user)

        logger.info('Creating author profile for new user.')
        author = Author(skills=user_data.get('skills'))
        return token, new_user, author

    @classmethod
    def login(cls, user_data, request):
        logger.info('Creating user model. Credentials - \n Email - {}\nPassword'.
                    format(user_data.get('email'), user_data.get('password')))

        user = authenticate(username=user_data.get('email'),
                            password=user_data.get('password'))
        if not user:
            raise Exception('Invalid credentials.')
        # django_login(request, user)
        logger.info('Creating Auth token.')
        token, created = Token.objects.get_or_create(user=user)

        return token, created

    @classmethod
    def logout(cls, user):
        logger.info('Removing token for user. {}'.format(user))
        Token.objects.get(user=user).delete()
        pass


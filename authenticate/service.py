from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class AuthenticationService(object):

    @classmethod
    def register(cls, user_data):
        User = get_user_model()
        new_user = User.objects.create_superuser(email=user_data.get('email'),
                                                 first_name=user_data.get('first_name'),
                                                 last_name=user_data.get('last_name'),
                                                 password=user_data.get('password'),
                                                 is_staff=True,
                                                 is_superuser=True)
        token, created = Token.objects.get_or_create(user=new_user)
        print('Returning token. {}'.format(token))

        return token, new_user

    @classmethod
    def login(cls, user_data, request):
        print('email - {}\nPassword - {}'.format(user_data.get('email'),
                                                 user_data.get('password')))
        user = authenticate(username=user_data.get('email'),
                            password=user_data.get('password'))
        if not user:
            raise Exception('Invalid credentials.')
        # django_login(request, user)
        print('Creating Auth token for {}'.format(user))
        token, created = Token.objects.get_or_create(user=user)
        print('Returning token. {}'.format(token))

        return token, created

    @classmethod
    def logout(cls, user):
        print('Removing token for user. {}'.format(user))
        Token.objects.get(user=user).delete()
        pass


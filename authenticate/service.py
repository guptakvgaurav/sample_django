from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class AuthenticationService(object):

    @classmethod
    def register(cls, user_data):
        User = get_user_model()
        new_user = User(username=user_data.get('username'),
                        email=user_data.get('email'),
                        first_name=user_data.get('first_name'),
                        last_name=user_data.get('last_name'),
                        is_staff=True,
                        is_superuser=True)
        new_user.set_password(user_data.get('password'))
        new_user.save()
        token, created = Token.objects.get_or_create(user=new_user)
        print('Returning token. {}'.format(token))

        return token, new_user

    @classmethod
    def login(cls, user_data, request):
        print('Username - {}\nPassword - {}'.format(user_data.get('username'),
                                                    user_data.get('password')))
        user = authenticate(request,
                            username=user_data.get('username'),
                            password=user_data.get('password'))
        print('Performing Django session login !!')
        # django_login(request, user)
        print('Creating Auth token for {}'.format(user.username))
        token, created = Token.objects.get_or_create(user=user)
        print('Returning token. {}'.format(token))

        return token, created

    @classmethod
    def logout(cls, user):
        print('Removing token for user. {}'.format(user))
        Token.objects.get(user=user).delete()
        pass


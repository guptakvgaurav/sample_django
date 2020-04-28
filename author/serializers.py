from rest_framework import serializers
from .models import Author
from core.serializers import UserSerializer


class KafkaAuthorSerializer(serializers.ModelSerializer):
    MESSAGE_TYPE = 'author'
    VERSION = 1
    KEY_FIELD = 'skills'

    user = UserSerializer
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Author
        fields = ['user', 'skills', 'email']

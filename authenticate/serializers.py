from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


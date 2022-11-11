from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name_user',
            'lastname_user',
            'email_user',
        )


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email_user = serializers.EmailField()

    class Meta:
        model = User
        fields = ('token', 'email_user', 'password_user')
        extra_kwargs = {
            'password_user': {
                'write_only': True
            },
        }

    def validate(self, data):
        user = get_object_or_404(User, email_user=data['email_user'])
        if not user.check_password(raw_password=data['password_user']):
            raise ValidationError("Contraseña incorrecta", status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token
        return data


class SignupSerializer(serializers.ModelSerializer):
    password_user = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email_user',
                  'name_user',
                  'lastname_user',
                  'password_user',
                  'password2')

        extra_kwargs = {"password_user": {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(
            email_user=validated_data['email_user'],
            name_user=validated_data['name_user'],
            lastname_user=validated_data['lastname_user'],
            password_user=validated_data['password_user']
        )

    def validate(self, attrs):
        if attrs['password_user'] != attrs['password2']:
            raise serializers.ValidationError({"password_user": "Passwords doesn't match."})
        return attrs

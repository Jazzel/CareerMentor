from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from .models import Score
>>>>>>> 3f793383a0fbee649f316c02a96636d4227ca046

# # User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# # Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
<<<<<<< HEAD
=======


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
>>>>>>> 3f793383a0fbee649f316c02a96636d4227ca046

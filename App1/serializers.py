from rest_framework import serializers
from django.contrib.auth.models import User

#from .models import Score
# # User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# # Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','city', 'country')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}


        def create(self, validated_data):
            return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],validated_data['city'],validated_data['country'])


#class ScoreSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Score
   #     fields = '__all__'



##
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # Serialize all fields in the model

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()  # Use the ProfileSerializer to serialize the related profile
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# ##Tody##
# from rest_framework import serializers
# from .models import CustomUser
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'city', 'country']
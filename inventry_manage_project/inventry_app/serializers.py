from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Item, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        

class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    # write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    # email = serializers.EmailField(
    # required=True,
    # validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["name"] = user.name + user.family

        return token
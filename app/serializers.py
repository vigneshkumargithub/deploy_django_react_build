# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username_or_email = data.get("username_or_email")
        password = data.get("password")

        try:
            user = User.objects.get(email=username_or_email)
        except User.DoesNotExist:
            user = None
        
        if user is None:
            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                user = None

        if user and user.check_password(password):
            return user
        
        raise serializers.ValidationError("Invalid login credentials.")
    

###### serializers for contact from

class ContactdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactdetail
        fields = '__all__'


class RecipientEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipientEmail
        fields='__all__'


##### realstate and homeproperty for serializers


from rest_framework import serializers
from .models import RealEstateProperty

class RealEstatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateProperty
        fields = '__all__'  # You can specify the fields you need here


# Home page home property

from rest_framework import serializers
from .models import Homeproperties

class HomepropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeproperties
        fields = ['id', 'title', 'description', 'price', 'location', 'image']



#### filled kyc details and bank details

# from rest_framework import serializers
# from .models import Kyc, BankDetails

# class BankDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BankDetails
#         fields = '__all__'

# class KycSerializer(serializers.ModelSerializer):
#     bank_details = BankDetailsSerializer(many=True, read_only=True)

#     class Meta:
#         model = Kyc
#         fields = '__all__'

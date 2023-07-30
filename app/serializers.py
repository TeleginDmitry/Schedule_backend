from rest_framework import serializers
from .models import TrainingClass, Staff, Room, Price
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        exclude = ['date_joined']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ['date_joined']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ['date_joined']

class PriceWithoutPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'name', 'description']




class TrainingClassSerializer(serializers.ModelSerializer):
    service = PriceWithoutPriceSerializer(read_only=True)
    trainer = StaffSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.service.price

    class Meta:
        model = TrainingClass
        exclude = ['date_joined']




class CustomTokenVerifySerializer(TokenVerifySerializer):
    user = UserSerializer(read_only=True) 

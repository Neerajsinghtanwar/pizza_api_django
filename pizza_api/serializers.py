from django.contrib.auth import models
from rest_framework.utils import field_mapping
from .models import Order, User, Pizza, Price, Topping
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True, required=True, help_text='Enter your password', style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(max_length=128, write_only=True, required=True, help_text='Enter your password again', style={'input_type': 'password', 'placeholder': 'Confirm-Password'})

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'user_type',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        ]
        read_only_fields = ['id', 'user_type']
        

    def validate(self, data):
        p1 = data.get('password')
        p2 = data.get('confirm_password')
        if p1 != p2:
            raise serializers.ValidationError({'msg': 'password does not match', 'password':p1, 'confirm_password':p2})
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['order_id', 'price']


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"
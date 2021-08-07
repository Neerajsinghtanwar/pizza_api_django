from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PizzaSerializer, UserSerializer, ToppingSerializer, OrderSerializer, PriceSerializer
from .models import Pizza, Topping, User, Order, Price
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
import pandas as pd
import uuid
from django.core.mail import send_mail
from pizza_api_django.settings import EMAIL_HOST_USER


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    search_fields = ['^name']
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(username=user)
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():        
            p = make_password(serializer.validated_data['password'])
            User.objects.create(first_name=serializer.validated_data['first_name'], last_name=serializer.validated_data['last_name'], email=serializer.validated_data['email'], username=serializer.validated_data['username'], password=p)

            # send welcome email:-
            # for receive email please set your mail-id and password in settings.py's Email section.
            subject = "Delecious Pizza Deleivery"
            message = f"Hello, {request.data['first_name']} Welcome to our Pizza App"
            email_from = EMAIL_HOST_USER
            email = request.data['email']
            # send_mail(subject, message, email_from, [email], fail_silently=False)

            return Response({'msg':'Created Successfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class StaffView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]

    search_fields = ['^name']
  
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():                   
            p = make_password(serializer.validated_data['password'])
            User.objects.create(first_name=serializer.validated_data['first_name'], last_name=serializer.validated_data['last_name'], email=serializer.validated_data['email'], username=serializer.validated_data['username'], password=p, is_staff=True)
            return Response({'msg':'Created Successfuly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class PizzaView(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class ToppingView(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            Price.objects.filter(id=1).update(price = request.data['price'])
            return Response({'msg':'Price Updated Successfuly'})
        return Response(serializer.errors)


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(username=user)


# create csv file of Users:- 
class ExportExcel(APIView):
    def get(self, request):
        user_obj = User.objects.all()
        serializer = UserSerializer(user_obj, many=True)
        file = pd.DataFrame(serializer.data)
        file.to_csv(f"pizza_api/static/excel/{uuid.uuid4()}.csv", encoding="UTF-8")
        return Response(serializer.data)

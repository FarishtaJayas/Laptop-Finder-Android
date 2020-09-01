from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class UserList(APIView):
    def get(self, request):
        model = Users.objects.all()
        serializer = UsersSerializers(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_user(self, user_id):
        try:
            model = Users.objects.get(id=user_id)
            return model
        except Users.DoesNotExist:
            return Response(f'User with {user_id} is Not Found', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, user_id):
        serializer = UsersSerializers(self.get_user(user_id))
        return Response(serializer.data)

    def put(self, request, user_id):
        serializer = UsersSerializers(self.get_user(user_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        model = self.get_user(user_id)
        model.delete()
        return Response(f'User with {user_id} is not found', status=status.HTTP_204_NO_CONTENT)


class Laptop_By_Brand(APIView):
    def get(self, request, laptop_brand):
        return Response(self.get_laptops_serialized(laptop_brand))

    @staticmethod    
    def get_laptops_serialized(laptop_brand):
        model = laptop_properties.objects.filter(lapBrand__icontains=laptop_brand)
        serializer = LaptopSerializers(model, many=True)
        return serializer.data


class Laptop_By_Price(APIView):
    def get(self, request, price):
        return Response(self.get_laptops_serialized(price))

    @staticmethod    
    def get_laptops_serialized(laptop_price):
        model = laptop_properties.objects.filter(price__lte=laptop_price).order_by('-price')
        serializer = LaptopSerializers(model, many=True)
        return serializer.data
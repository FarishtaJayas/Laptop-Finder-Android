from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.database_manager.api import Laptop_By_Brand, Laptop_By_Price


class Text_Analyzer(APIView):
    def get(self, request, text):
        return Response(Laptop_By_Brand.get_laptops_serialized(laptop_brand=text), status=status.HTTP_200_OK, headers={"Access-Control-Allow-Origin":"*"})
    
class Laptops_By_Price(APIView):
    def get(self, request, laptop_price):
        return Response(Laptop_By_Price.get_laptops_serialized(laptop_price=int(laptop_price)), status=status.HTTP_200_OK, headers={"Access-Control-Allow-Origin":"*"})
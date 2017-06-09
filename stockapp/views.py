from django.shortcuts import get_object_or_404  
from rest_framework.views import APIView #to return API data
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializers

#Lists all stocks or create a new one
# stocks/
class StockList(APIView):

	def get(self,request): #user get the list of all companies
		stocks = Stock.objects.all()
		serializers = StockSerializers(stocks, many=True) #get the data and convert it into JSON
		return Response(serializers.data) #return json data

	def post(self): #submitting a forum.let him add new objects
		pass
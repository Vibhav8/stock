from rest_framework import serializers
# serializers are used to save data in a format which can be shared on hard drive or share over network
from .models import Stock

class StockSerializers(serializers.ModelSerializer):

	class Meta:
		model = Stock
		#fields = ('ticker','volume') : if u want to include some models
		fields = '__all__' #include all model fields
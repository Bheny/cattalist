from rest_framework.serializers import ModelSerializer 

from .models import * 

class ListingsSerializer(ModelSerializer):
	class Meta:
		model = Listing 
		fields = '__all__'
		depth = 2


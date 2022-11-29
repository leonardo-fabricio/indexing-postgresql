from rest_framework import serializers
from Aplicacao.models import *

class ProductSerializer(serializers.ModelSerializer):
      class Meta:
            model = ModelProduct
            fields = ("__all__")

class ClientsSerializer(serializers.ModelSerializer):
      class Meta:
            model = Clients
            fields = ("__all__")
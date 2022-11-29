from rest_framework import generics
from rest_framework.response import Response
from .serializer import *

class CreateProduct(generics.CreateAPIView):
      serializer_class = ProductSerializer

class ClientsProduct(generics.CreateAPIView):
      serializer_class = ClientsSerializer

class ListClient(generics.ListAPIView):
      serializer_class = ClientsSerializer
      def list(self, request, *args, **kwargs):
            print(Clients.objects.all().query)
            return Response(Clients.objects.all().values_list("name", flat=True))
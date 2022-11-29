from django.urls import path
from .views import *

urlpatterns = [
    path("criar_produto", CreateProduct.as_view()),
    path("criar_clientes", ClientsProduct.as_view()),
    path("listar", ListClient.as_view())
]
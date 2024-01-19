from django.urls import path
from mainapp.views import index, products, product, about, contact

urlpatterns = [
    path('', index),
    path('products/', products),
    path('product/', product),
    path('about/', about),
    path('contact/', contact),
]

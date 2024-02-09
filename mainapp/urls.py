from django.urls import path
from mainapp.views import index, products, product, about, contact

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/', product, name='product'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def product(request):
    return render(request, 'product.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')



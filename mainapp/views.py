from django.shortcuts import render


def get_menu(key):
    links_menu = [
        {'href': 'main:index', 'name': 'Home', 'active': False},
        {'href': 'main:products', 'name': 'Products', 'active': False},
        {'href': 'main:about', 'name': 'About', 'active': False},
        {'href': 'main:contact', 'name': 'Contact', 'active': False},
    ]

    for item in links_menu:
        if item['href'].split(':')[1] == key:
            item['active'] = True

    return links_menu


def index(request):

    title = 'The main page'

    context = {
        'title': title,
        'links_menu': get_menu('index'),
    }

    return render(request, 'index.html', context)


def products(request):

    title = 'The products page'

    context = {
        'title': title,
        'links_menu': get_menu('products'),
    }
    return render(request, 'products.html', context)


def product(request):

    title = 'The product page'

    context = {
        'title': title,
    }
    return render(request, 'product.html', context)


def about(request):

    title = 'The about page'

    context = {
        'title': title,
        'links_menu': get_menu('about'),
    }
    return render(request, 'about.html', context)


def contact(request):

    title = 'The contact page'

    context = {
        'title': title,
        'links_menu': get_menu('contact'),
    }
    return render(request, 'contact.html', context)



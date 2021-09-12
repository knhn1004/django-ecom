from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Category, Product

#def index(req):

#    text = 'Hello World'
#    return HttpResponse(text)


class IndexView(TemplateView):
    template_name = 'index.html'


def all_categories_view(req, cat_slug=None):
    cat = None
    products = None
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=cat, available=True)
    else:
        products = Product.objects.filter(available=True)

    return render(req, 'shop/category.html', {
        'category': cat,
        'products': products
    })
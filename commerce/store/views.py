from django.shortcuts import render
from . models import Catergory, Product
from django.shortcuts import get_object_or_404

# Create your views here.

def store(request):

    all_products = Product.objects.all()

    context = {'all_products': all_products}

    return render(request, 'store/store.html', context)


def categories(request):
    all_categories = Catergory.objects.all()
    return{'all_categories': all_categories} 



def list_category(request, slug=None):

    category = get_object_or_404(Catergory, slug=slug)

    products = Product.objects.filter(category=category)


    return render(request, 'store/list-category.html', {'category':category, 'products':products})


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}

    return render(request, 'store/product-info.html', context)
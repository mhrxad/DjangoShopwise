from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


# region " Partial View Code Behind "
def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products_categories_partial.html', context)


# endregion


class ProductsList(ListView):
    template_name = 'products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']
    product = Product.objects.get_by_id(product_id)

    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


class ProductsListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه ی مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)


class SearchProductsView(ListView):
    template_name = 'products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()

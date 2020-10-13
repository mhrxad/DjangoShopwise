from django.urls import path

from .views import *

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),

    path('products_categories_partial', products_categories_partial, name='products_categories_partial')

]

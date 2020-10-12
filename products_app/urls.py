from django.urls import path

from .views import *

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
]

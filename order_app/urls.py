from django.urls import path

from .views import *

urlpatterns = [
    path('add-user-order', add_user_order),
    path('open-order', user_open_order),

]

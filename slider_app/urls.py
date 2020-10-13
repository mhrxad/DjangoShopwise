from django.urls import path

from .views import *

urlpatterns = [
    path('slider', slider, name="Slider"),
]

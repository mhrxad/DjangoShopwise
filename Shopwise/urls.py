"""Shopwise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import settings
from .views import *

urlpatterns = [
    path('', home_page),

    path('top-header', top_header, name="TopHeader"),
    path('bottom-header', bottom_header, name="BottomHeader"),
    path('top-footer', top_footer, name="TopFooter"),
    path('bottom-footer', bottom_footer, name="BottomFooter"),
    path('slider', slider, name="Slider"),
    path('double-banner', double_banner, name="DoubleBanner"),
    path('banner', banner, name="Banner"),
    path('testimonial', testimonial, name="Testimonial"),
    path('shop-info', shop_info, name="ShopInfo"),
    path('news-letter', news_letter, name="NewsLetter"),

    path('admin/', admin.site.urls)
]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

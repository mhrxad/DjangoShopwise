from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about-us', about_us_page, name='AboutUs'),

    path('', include('account_app.urls')),
    path('', include('products_app.urls')),
    path('', include('slider_app.urls')),
    path('', include('contact_app.urls')),
    path('', include('order_app.urls')),

    path('top-header', top_header, name="TopHeader"),
    path('middle-header', middle_header, name="MiddleHeader"),
    path('bottom-header', bottom_header, name="BottomHeader"),
    path('top-footer', top_footer, name="TopFooter"),
    path('bottom-footer', bottom_footer, name="BottomFooter"),
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

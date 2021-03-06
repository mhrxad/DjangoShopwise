# region " imports "
from django.shortcuts import render

# endregion


# region " Partial View Code Behind "
from setting_app.models import SiteSetting


def top_header(request, *args, **kwargs):
    context = {
        'phoneNumber': '12345678'
    }
    return render(request, 'shared/_TopHeader.html', context)


def middle_header(request, *args, **kwargs):
    setting = SiteSetting.objects.first()

    context = {
        'setting': setting
    }
    return render(request, 'shared/_MiddleHeader.html', context)


def bottom_header(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_BottomHeader.html', context)


def top_footer(request, *args, **kwargs):
    setting = SiteSetting.objects.first()

    context = {
        'setting': setting
    }
    return render(request, 'shared/_TopFooter.html', context)


def bottom_footer(request, *args, **kwargs):
    setting = SiteSetting.objects.first()

    context = {
        'setting': setting
    }
    return render(request, 'shared/_BottomFooter.html', context)


def double_banner(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_DoubleBanner.html', context)


def banner(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_Banner.html', context)


def testimonial(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_Testimonial.html', context)


def shop_info(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_ShopInfo.html', context)


def news_letter(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/_NewsLetter.html', context)


# endregion


# region " Pages Code Behind"

def home_page(request):
    context = {
        'title': 'Shopwise'
    }
    return render(request, 'Pages/home.html', context)


def about_us_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'title': 'درباره ما',
        'setting': site_setting
    }
    return render(request, 'Pages/AboutUs.html', context)

# endregion

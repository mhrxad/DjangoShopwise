from django.shortcuts import render
from slider_app.models import Slider


# region " Partial View Code Behind "

def slider(request, *args, **kwargs):
    sliders = Slider.objects.all()
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'sliders': sliders
    }
    return render(request, 'Slider_PartialView.html', context)

# endregion

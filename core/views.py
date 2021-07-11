from django.shortcuts import render

from sliders.models import Slider


def index(request):
    sliders = Slider.objects.filter(is_active=True)
    context = {
        'sliders': sliders,
    }
    return render(request, 'core/index.html', context)

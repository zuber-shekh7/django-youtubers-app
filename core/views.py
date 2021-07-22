from django.shortcuts import render

from sliders.models import Slider


def index(request):
    sliders = Slider.objects.filter(is_active=True)
    context = {
        'sliders': sliders,
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def developer(request):
    return render(request, 'core/developer.html')

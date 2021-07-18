from django.shortcuts import render

from .models import Youtuber


def list_youtubers(request):
    youtubres = Youtuber.objects.all()
    context = {
        'youtubers': youtubres,
    }
    return render(request, 'youtubers/list.html', context)

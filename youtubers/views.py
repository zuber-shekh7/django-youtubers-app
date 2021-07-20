from django.shortcuts import render, get_object_or_404

from .models import Youtuber


def list_youtubers(request):
    youtubres = Youtuber.objects.all()
    context = {
        'youtubers': youtubres,
    }
    return render(request, 'youtubers/list.html', context)


def detail_youtuber(request, pk):
    youtuber = get_object_or_404(Youtuber, pk=pk)
    context = {
        'youtuber': youtuber,
    }
    return render(request, 'youtubers/detail.html', context)

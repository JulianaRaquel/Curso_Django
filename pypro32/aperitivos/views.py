from django.shortcuts import render, get_object_or_404
from pypro32.aperitivos.models import Video


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video.html', context={'video': video})

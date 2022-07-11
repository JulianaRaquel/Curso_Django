from django.shortcuts import render

class Video:
    def __init__(self, slug, video, vimeo_id):
        self.slug = slug
        self.video = video
        self.video_id = vimeo_id

videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação', 726398954),
    Video('instalacao-windows', 'Instalação Windows', 251497668),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'video.html', context={'video': video})

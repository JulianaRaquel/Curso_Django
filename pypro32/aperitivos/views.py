
from django.shortcuts import render

def video(request, slug):
    return render(request, 'video.html')

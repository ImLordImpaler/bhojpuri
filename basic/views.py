from django.shortcuts import render
from .models import Video
# Create your views here.


def homepage(request):
    vid = Video.objects.all()
    params = {
        'vid' : vid
    }
    return render(request , 'basic/index.html' , params)

def videoDetail(request , pk):
    vid = Video.objects.get(id=pk)
    params = {
        'video' : vid
    }
    return render(request , 'basic/video-detail.html' , params)
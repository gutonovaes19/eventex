from django.shortcuts import render
from django.http import HttpResponse
from eventex.core.models import Speaker

# Create your views here.

def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
    ]
    return render(request,'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    return render(request,'core/speaker_detail.html', {'speaker':Speaker()})

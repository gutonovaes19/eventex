from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from eventex.core.models import Speaker

# Create your views here.

def home(request):
    speakers = Speaker.objetcs.all()
    return render(request,'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    #instanciamos um speaker sem gravar no banco
    #speaker = Speaker.objects.get(slug=slug)
    speaker = get_object_or_404(Speaker,slug=slug)
    return render(request,'core/speaker_detail.html', {'speaker':speaker})

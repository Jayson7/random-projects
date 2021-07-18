from django.shortcuts import render
from video import models 
from video.models import Video
from pdf import models 
from pdf.models import pdf
from audio import models 
from audio.models import Audio

# Create your views here.

def homeMainView(request):
    videorender = Video.objects.all()
    videorenders = videorender[0:9]
    pdfs = pdf.objects.all()
    pdfStuff = pdfs[0:3]
    pdfStuffs = pdfs[3:6]
    audios = Audio.objects.all()
    audioStuffs = audios[:3]
    audioStuff = audios[3:6]

    return render(request, "index.html", {"videorenders": videorenders, "pdfStuff":pdfStuff, "pdfStuffs":pdfStuffs,"audioStuffs":audioStuffs,"audioStuff":audioStuff})
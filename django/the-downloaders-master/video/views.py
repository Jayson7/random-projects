from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Video
from django.contrib import messages

# Create your views here.
from .filters import VideoFilter
class videoView(ListView):
    model = Video
    template_name = "video/home.html"
    fields = "__all__"


def video_list(request):
    
    filter = VideoFilter(request.GET, queryset=Video.objects.all())

    return render(request, 'video/search.html', {'filter': filter})
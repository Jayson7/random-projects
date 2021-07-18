from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Audio
from .filter import AudioFilter
# Create your views here.

class audioView(ListView):
    model = Audio
    template_name = "audio/home.html"
    fields = "__all__"

def Audio_list(request):
    
    filter = AudioFilter(request.GET, queryset=Audio.objects.all())

    return render(request, 'audio/search.html', {'filter': filter})
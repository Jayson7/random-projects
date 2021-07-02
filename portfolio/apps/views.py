from django.shortcuts import render
from .models import App, AppFilter

# Create your views here.

def home(request):
    context = {}
    context["projects"] = App.objects.all()
    context['filter'] = AppFilter(request.GET, queryset=App.objects.all())
    
    return render(request, "index.html", {'context':context})
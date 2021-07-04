from django.shortcuts import render
from .models import App, AppFilter, Category
from django.views.generic import TemplateView
import django_filters
# Create your views here.



class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["projects"] = App.objects.all()
        context["categories"] = Category.objects.all()
       
        return context


def Searchlist(request):
    filter = AppFilter(request.GET, queryset=App.objects.all())
    return render(request, 'search.html', {'filter': filter})

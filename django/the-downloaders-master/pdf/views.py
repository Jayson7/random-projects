
# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import pdf
from .filters import PdfFilter
# Create your views here.

class pdfView(ListView):
    model = pdf
    template_name = "pdf/home.html"
    fields = "__all__"


def pdf_list(request):
    
    filter = PdfFilter(request.GET, queryset=pdf.objects.all())

    return render(request, 'pdf/search.html', {'filter': filter})

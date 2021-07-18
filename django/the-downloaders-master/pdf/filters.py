import django_filters
from .models import pdf

class PdfFilter(django_filters.FilterSet):
    

    class Meta:
        model = pdf
        fields = ['Title']
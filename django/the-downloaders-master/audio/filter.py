import django_filters
from .models import Audio

class AudioFilter(django_filters.FilterSet):
    

    class Meta:
        model = Audio
        fields = ['Title']
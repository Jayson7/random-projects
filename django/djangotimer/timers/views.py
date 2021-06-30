from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.


def home(request):

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # convert to string
    html = "Time is {}".format(current_time)
    # return response
    return render(request, "index.html", {"html": html} )
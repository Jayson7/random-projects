
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):


    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1c7814cffa14a394facc2f795beacab3'

    city = 'Las Vegas'
    cities = City.objects.all()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list
    
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    context = {'weather_data' : weather_data, 'form' : form} 

   
    return render(request, 'main/index.html') #returns the index.html template	

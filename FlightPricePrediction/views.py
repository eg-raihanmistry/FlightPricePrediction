from django.shortcuts import render
import pickle
import os
from django.conf import settings

path = os.path.join(settings.BASE_DIR, 'flight_price_prediction_model.pkl')
with open(path, "rb") as file:
    model = pickle.load(file)

def home(request):
    price = None
    if request.method == "POST":
        airline = request.POST['airline']
        source_city = request.POST['source_city']
        departure_time = request.POST['departure_time']
        stops = request.POST['stops']
        arrival_time = request.POST['arrival_time']
        destination_city = request.POST['destination_city']
        flight_class = request.POST['class']
        duration = request.POST['duration']
        days_left = request.POST['days_left']

        data = [[airline, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left]]
        price = model.predict(data)

    context = {
        'price' : price
    }

    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
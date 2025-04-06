from django.shortcuts import render, redirect
from . models import Flight, SiteVisits
from .forms import AirlineForm, CityForm, FlightForm


def index(request):
    visit, created = SiteVisits.objects.get_or_create(pk=1)
    visit.count += 1
    visit.save()

    return render(request, "flights/index.html", {
        "visit_count": visit.count,
    })


def flights(request):
    flights = Flight.objects.all()
    return render(request, "flights/flights.html", {
        "flights": flights,
    })


def create_forms(request):
    if request.method == "POST":
        airline_form = AirlineForm(request.POST)
        city_form = CityForm(request.POST)
        flight_form = FlightForm(request.POST)

        if airline_form.is_valid():
            airline_form.save()
            return redirect('create-forms')  

        if city_form.is_valid():
            city_form.save()
            return redirect('create-forms')

        if flight_form.is_valid():
            flight_form.save()
            return redirect('create-forms')

    else:
        airline_form = AirlineForm()
        city_form = CityForm()
        flight_form = FlightForm()

    return render(request, "flights/forms.html", {
        "airline_form": airline_form,
        "city_form": city_form,
        "flight_form": flight_form,
    })


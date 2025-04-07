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
        form_type = request.POST.get("form_type")

        if form_type == "airline":
            airline_form = AirlineForm(request.POST)
            if airline_form.is_valid():
                airline_form.save()
                return redirect('create-forms')
            city_form = CityForm()
            flight_form = FlightForm()

        elif form_type == "city":
            city_form = CityForm(request.POST)
            if city_form.is_valid():
                city_form.save()
                return redirect('create-forms')
            airline_form = AirlineForm()
            flight_form = FlightForm()

        elif form_type == "flight":
            flight_form = FlightForm(request.POST)
            if flight_form.is_valid():
                flight_form.save()
                return redirect('create-forms')
            airline_form = AirlineForm()
            city_form = CityForm()

    else:
        airline_form = AirlineForm()
        city_form = CityForm()
        flight_form = FlightForm()

    return render(request, "flights/forms.html", {
        "airline_form": airline_form,
        "city_form": city_form,
        "flight_form": flight_form,
    })



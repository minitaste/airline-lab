from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="flights")
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin_flights')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destenation_flights')
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    price = models.PositiveIntegerField()
    flight_id = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f"{self.origin} - {self.destination}"
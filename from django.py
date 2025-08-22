from django.test import TestCase
from .models import Flight
from django.core.exceptions import ValidationError

# flights/test_models.py


class FlightModelTest(TestCase):
    def test_create_flight_valid(self):
        flight = Flight.objects.create(
            name="Vuelo 101",
            flight_type=Flight.NATIONAL,
            price=150.00
        )
        self.assertEqual(flight.name, "Vuelo 101")
        self.assertEqual(flight.flight_type, Flight.NATIONAL)
        self.assertEqual(flight.price, 150.00)

    def test_str_representation(self):
        flight = Flight.objects.create(
            name="Vuelo 202",
            flight_type=Flight.INTERNATIONAL,
            price=300.00
        )
        expected = "Vuelo 202 (Internacional) - $300.00"
        self.assertEqual(str(flight), expected)

    def test_price_validator(self):
        flight = Flight(
            name="Vuelo 303",
            flight_type=Flight.NATIONAL,
            price=-10.00
        )
        with self.assertRaises(ValidationError):
            flight.full_clean()

    def test_ordering_by_price(self):
        Flight.objects.create(name="A", flight_type=Flight.NATIONAL, price=200.00)
        Flight.objects.create(name="B", flight_type=Flight.NATIONAL, price=100.00)
        Flight.objects.create(name="C", flight_type=Flight.NATIONAL, price=300.00)
        flights = list(Flight.objects.all())
        prices = [f.price for f in flights]
        self.assertEqual(prices, sorted(prices))
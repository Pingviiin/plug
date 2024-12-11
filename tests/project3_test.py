from PROJECT.project3.vehicle_rental import *
import pytest
from datetime import datetime

"""
@pytest.fixture
def setup_vehicle_rental():
    rental = VehicleRental()

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Toyota", "Corolla", 2018, Type.OTHER)
    motorcycle1 = Motorcycle("Yamaha", "R1", 2019)
    motorcycle2 = Motorcycle("Kawasaki", "Ninja", 2020)

    client1 = Client("Alice", 500)
    client2 = Client("Bob", 400)

    rental.clients.extend([client1, client2])
    rental.booked_cars[car1] = ["01.01.2024", "02.01.2024"]
    rental.booked_cars[car2] = ["01.01.2024"]
    rental.booked_cars[motorcycle1] = ["01.01.2024", "02.01.2024", "03.01.2024"]
    rental.booked_cars[motorcycle2] = ["01.01.2024"]

    return rental, car1, car2, motorcycle1, motorcycle2

def test_no_rentals(setup_vehicle_rental):
    rental, *_ = setup_vehicle_rental
    rental.booked_cars = {}
    assert rental.get_most_rented_vehicle() == []

def test_single_most_rented_vehicle(setup_vehicle_rental):
    rental, _, _, motorcycle1, _ = setup_vehicle_rental
    assert rental.get_most_rented_vehicle() == [motorcycle1]

def test_multiple_most_rented_vehicles(setup_vehicle_rental):
    rental, car1, _, motorcycle1, _ = setup_vehicle_rental
    # Make car1 and motorcycle1 tied for most rentals
    rental.booked_cars[car1].append("03.01.2024")
    assert set(rental.get_most_rented_vehicle()) == {car1, motorcycle1}

def test_all_vehicles_tied(setup_vehicle_rental):
    rental, car1, car2, motorcycle1, motorcycle2 = setup_vehicle_rental
    rental.booked_cars[car1] = ["01.01.2024"]
    rental.booked_cars[car2] = ["01.01.2024"]
    rental.booked_cars[motorcycle1] = ["01.01.2024"]
    rental.booked_cars[motorcycle2] = ["01.01.2024"]
    assert set(rental.get_most_rented_vehicle()) == {car1, car2, motorcycle1, motorcycle2}

def test_edge_case_empty_bookings(setup_vehicle_rental):
    rental, car1, car2, motorcycle1, motorcycle2 = setup_vehicle_rental
    rental.booked_cars = {
        car1: [],
        car2: [],
        motorcycle1: [],
        motorcycle2: []
    }
    assert rental.get_most_rented_vehicle() == []

def test_add_vehicle_successful():
    rental = VehicleRental()
    car = Car("Toyota", "Corolla", 2022, Type.OTHER)
    
    assert rental.add_vehicle(car) is True  # Should add successfully
    assert car in rental.booked_cars  # Check if car was added

def test_add_vehicle_duplicate():
    rental = VehicleRental()
    car = Car("Toyota", "Corolla", 2022, Type.OTHER)
    rental.add_vehicle(car)  # Add the car once

    assert rental.add_vehicle(car) is False  # Adding again should fail
    assert len(rental.booked_cars) == 1  # Only one car should be present

def test_add_multiple_vehicles():
    rental = VehicleRental()
    car1 = Car("Toyota", "Corolla", 2022, Type.OTHER)
    car2 = Car("Honda", "Civic", 2023, Type.CONVERTIBLE)
    
    assert rental.add_vehicle(car1) is True  # Add first car
    assert rental.add_vehicle(car2) is True  # Add second car
    assert len(rental.booked_cars) == 2  # Both cars should be added

def test_add_vehicle_hash_collision():
    rental = VehicleRental()
    car1 = Car("Toyota", "Corolla", 2022, Type.OTHER)
    car2 = Car("Toyota", "Corolla", 2022, Type.OTHER)  # Same attributes, should collide

    assert rental.add_vehicle(car1) is True
    assert rental.add_vehicle(car2) is False  # Should not add duplicate
    assert len(rental.booked_cars) == 1  # Only one car stored

"""

@pytest.fixture
def setup_rental():
    rental = VehicleRental()
    client = Client("John Doe", 500)
    car = Car("Toyota", "Camry", 2020, Type.OTHER)
    motorcycle = Motorcycle("Yamaha", "R1", 2022)
    return rental, client, car, motorcycle

def test_rent_vehicle_success():
    rental_system = VehicleRental()
    car = Car("Toyota", "Camry", 2020, Type.SPORTSCAR)
    client = Client("Alice", budget=300)  # Budget sufficient for a SPORTSCAR
    rental_system.add_vehicle(car)

    result = rental_system.rent_vehicle(car, "12.12.2024", client)

    assert result is True
    assert client.budget == 100  # Budget reduced by the price of a SPORTSCAR (200)
    assert "12.12.2024" in car.rent_dates  # Ensure the vehicle's date is updated
    assert rental_system.balance == 200  # Rental system's balance updated by the price of a SPORTSCAR


def test_rent_vehicle_insufficient_funds(setup_rental):
    rental, client, car, _ = setup_rental
    client.budget = 10  # Insufficient funds
    rental.add_vehicle(car)
    assert rental.rent_vehicle(car, "12.12.2024", client) is False
    assert rental.get_money() == 0

def test_rent_vehicle_already_booked(setup_rental):
    rental, client, car, _ = setup_rental
    rental.add_vehicle(car)
    rental.rent_vehicle(car, "12.12.2024", client)
    assert rental.rent_vehicle(car, "12.12.2024", client) is False

def test_rent_vehicle_date_conflict(setup_rental):
    rental, client, car, _ = setup_rental
    rental.add_vehicle(car)
    rental.rent_vehicle(car, "12.12.2024", client)
    another_client = Client("Jane Doe", 500)
    assert rental.rent_vehicle(car, "12.12.2024", another_client) is False

def test_rent_vehicle_not_added(setup_rental):
    rental, client, car, _ = setup_rental
    assert rental.rent_vehicle(car, "12.12.2024", client) is False
    assert rental.get_money() == 0

def test_rent_vehicle_invalid_date(setup_rental):
    rental, client, car, _ = setup_rental
    rental.add_vehicle(car)
    assert rental.rent_vehicle(car, "", client) is False  # Invalid date
    assert rental.rent_vehicle(car, None, client) is False  # None date

def test_rent_vehicle_invalid_client(setup_rental):
    rental, _, car, _ = setup_rental
    rental.add_vehicle(car)
    assert rental.rent_vehicle(car, "12.12.2024", None) is False  # None client

def test_rent_vehicle_invalid_vehicle(setup_rental):
    rental, client, _, _ = setup_rental
    assert rental.rent_vehicle(None, "12.12.2024", client) is False  # None vehicle

def test_rent_vehicle_hash_collision(setup_rental):
    rental, client, car, motorcycle = setup_rental
    # Force hash collision by overriding hash methods
    car.__hash__ = lambda: 42
    motorcycle.__hash__ = lambda: 42

    rental.add_vehicle(car)
    rental.add_vehicle(motorcycle)

    assert rental.rent_vehicle(car, "12.12.2024", client) is True
    assert rental.rent_vehicle(motorcycle, "12.12.2024", client) is True
    assert rental.get_money() == car.get_price() + motorcycle.get_price()

def test_get_best_client_no_clients():
    rental = VehicleRental()
    result = rental.get_best_client()
    assert result is None, "Expected None when no clients are in the rental system."

def test_get_best_client_single_client():
    rental = VehicleRental()
    client = Client("Alice", budget=100)
    rental.clients.append(client)
    result = rental.get_best_client()
    assert result == client, "Expected the single client to be the best client."

def test_get_best_client_most_bookings():
    rental = VehicleRental()
    client1 = Client("Alice", budget=500)
    client2 = Client("Bob", budget=500)
    rental.clients.extend([client1, client2])

    car1 = Car("Toyota", "Camry", 2020, Type.SPORTSCAR)
    car2 = Car("Honda", "Civic", 2019, Type.CONVERTIBLE)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.rent_vehicle(car1, "12.12.2024", client1)
    rental.rent_vehicle(car2, "13.12.2024", client1)
    rental.rent_vehicle(car1, "14.12.2024", client2)

    result = rental.get_best_client()
    assert result == client1, "Expected the client with the most bookings to be the best client."

def test_get_best_client_tied_bookings_high_spender():
    rental = VehicleRental()
    client1 = Client("Alice", budget=1000)
    client2 = Client("Bob", budget=1000)
    rental.clients.extend([client1, client2])

    car1 = Car("Toyota", "Camry", 2020, Type.SPORTSCAR)
    car2 = Car("Honda", "Civic", 2019, Type.CONVERTIBLE)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.rent_vehicle(car1, "12.12.2024", client1)
    rental.rent_vehicle(car2, "13.12.2024", client2)
    rental.rent_vehicle(car2, "14.12.2024", client1)  # Alice spends more

    result = rental.get_best_client()
    assert result == client1, "Expected the high spender to be the best client in case of tied bookings."

def test_get_best_client_all_tied():
    rental = VehicleRental()
    client1 = Client("Alice", budget=500)
    client2 = Client("Bob", budget=500)
    rental.clients.extend([client1, client2])

    car = Car("Toyota", "Camry", 2020, Type.SPORTSCAR)

    rental.add_vehicle(car)
    rental.rent_vehicle(car, "12.12.2024", client1)
    rental.rent_vehicle(car, "13.12.2024", client2)

    result = rental.get_best_client()
    assert result in [client1, client2], "Expected either client in case of a complete tie."

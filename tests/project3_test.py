from PROJECT.project3.vehicle_rental import *
import pytest
from datetime import datetime

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

def test_get_best_client_single_best():
    rental = VehicleRental()

    client1 = Client("Alice", 500)
    client2 = Client("Bob", 500)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Tesla", "Model S", 2022, Type.CONVERTIBLE)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)
    rental.rent_vehicle(car2, "2024-12-02", client2)

    best_client = rental.get_best_client()
    assert best_client == client1 or best_client == client2, "The best client should be Alice or Bob."

def test_get_best_client_by_spent():
    rental = VehicleRental()

    client1 = Client("Alice", 1000)
    client2 = Client("Bob", 500)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Toyota", "Camry", 2021, Type.OTHER)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice spends 200
    rental.rent_vehicle(car2, "2024-12-02", client2)  # Bob spends 50

    best_client = rental.get_best_client()
    assert best_client == client1, "Alice should be the best client based on money spent."

def test_get_best_client_tie_rented():
    rental = VehicleRental()

    client1 = Client("Alice", 1000)
    client2 = Client("Bob", 1000)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Tesla", "Model S", 2022, Type.CONVERTIBLE)
    car3 = Car("Toyota", "Camry", 2021, Type.OTHER)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)
    rental.add_vehicle(car3)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice rents car1
    rental.rent_vehicle(car2, "2024-12-02", client1)  # Alice rents car2

    rental.rent_vehicle(car3, "2024-12-03", client2)  # Bob rents car3
    rental.rent_vehicle(car2, "2024-12-04", client2)  # Bob rents car2

    best_client = rental.get_best_client()
    assert best_client == client1 or best_client == client2, "The best client should be Alice or Bob due to tie."

def test_get_best_client_no_clients():
    rental = VehicleRental()
    best_client = rental.get_best_client()
    assert best_client is None, "No clients should result in None being returned."

def test_get_best_client_multiple_clients_tie_but_one_spent_more():
    rental = VehicleRental()

    client1 = Client("Alice", 1000)
    client2 = Client("Bob", 1000)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Tesla", "Model S", 2022, Type.CONVERTIBLE)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice spends 200
    rental.rent_vehicle(car2, "2024-12-02", client2)  # Bob spends 150
    rental.rent_vehicle(car2, "2024-12-03", client1)  # Alice spends another 150

    best_client = rental.get_best_client()
    assert best_client == client1, "Alice should be the best client as she spent more money despite tie in rentals."

def test_get_best_client_with_equal_rentals_and_equal_spent():
    rental = VehicleRental()

    client1 = Client("Alice", 1000)
    client2 = Client("Bob", 1000)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)
    car2 = Car("Tesla", "Model S", 2022, Type.CONVERTIBLE)

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice rents car1
    rental.rent_vehicle(car2, "2024-12-02", client1)  # Alice rents car2

    rental.rent_vehicle(car1, "2024-12-03", client2)  # Bob rents car1
    rental.rent_vehicle(car2, "2024-12-04", client2)  # Bob rents car2

    best_client = rental.get_best_client()
    assert best_client in [client1, client2], "Either Alice or Bob could be the best client due to exact tie."

def test_get_best_client_single_client_no_bookings():
    rental = VehicleRental()

    client1 = Client("Alice", 500)

    rental.clients.append(client1)

    best_client = rental.get_best_client()
    assert best_client is None, "A single client with no bookings should not be the best client."

def test_get_best_client_multiple_clients_no_bookings():
    rental = VehicleRental()

    client1 = Client("Alice", 500)
    client2 = Client("Bob", 500)

    rental.clients.extend([client1, client2])

    best_client = rental.get_best_client()
    assert best_client is None, "Multiple clients with no bookings should result in None."

def test_get_best_client_client_with_most_expensive_booking():
    rental = VehicleRental()

    client1 = Client("Alice", 1000)
    client2 = Client("Bob", 1000)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)  # Price: 200
    car2 = Car("Toyota", "Camry", 2021, Type.OTHER)      # Price: 50

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice spends 200
    rental.rent_vehicle(car2, "2024-12-02", client2)  # Bob spends 50

    best_client = rental.get_best_client()
    assert best_client == client1, "Alice should be the best client as she made the most expensive booking."

def test_get_best_client_multiple_clients_with_different_booking_counts():
    rental = VehicleRental()

    client1 = Client("Alice", 1500)
    client2 = Client("Bob", 1500)

    car1 = Car("Ford", "Mustang", 2020, Type.SPORTSCAR)  # Price: 200
    car2 = Car("Tesla", "Model S", 2022, Type.CONVERTIBLE)  # Price: 150

    rental.add_vehicle(car1)
    rental.add_vehicle(car2)

    rental.clients.extend([client1, client2])

    rental.rent_vehicle(car1, "2024-12-01", client1)  # Alice rents car1
    rental.rent_vehicle(car2, "2024-12-02", client1)  # Alice rents car2
    rental.rent_vehicle(car2, "2024-12-03", client2)  # Bob rents car2

    best_client = rental.get_best_client()
    assert best_client == client1, "Alice should be the best client as she rented more vehicles."

def test_book_vehicle_edge_cases():
    rental = VehicleRental()
    car = Car(make="Toyota", model="Corolla", year=2020, type_of_car=Type.VAN)
    motorcycle = Motorcycle(make="Yamaha", model="R1", year=2019)

    client = Client(name="Alice", budget=150)

    # Add vehicles to the rental system
    rental.add_vehicle(car)
    rental.add_vehicle(motorcycle)

    # 1. Client has insufficient funds
    client_insufficient = Client(name="Bob", budget=50)
    assert not client_insufficient.book_vehicle(car, "01.01.2024", rental), "Should fail due to insufficient funds"

    # 2. Vehicle already booked on the specified date
    rental.rent_vehicle(car, "01.01.2024", client)
    assert not client.book_vehicle(car, "01.01.2024", rental), "Should fail as vehicle is already booked"

    # 3. Invalid date format
    assert not client.book_vehicle(car, "2024-01-01", rental), "Should fail due to invalid date format"

    # 4. Vehicle does not exist in the rental system
    new_car = Car(make="Honda", model="Civic", year=2022, type_of_car=Type.CONVERTIBLE)
    assert not client.book_vehicle(new_car, "01.01.2024", rental), "Should fail as vehicle is not in the rental system"

    # 6. Vehicle is not added to the system before booking
    car_not_added = Car(make="Ford", model="Focus", year=2018, type_of_car=Type.OTHER)
    assert not client.book_vehicle(car_not_added, "01.01.2024", rental), "Should fail as vehicle is not added to the system"

    # 7. VehicleRental system has no vehicles
    empty_rental = VehicleRental()
    assert not client.book_vehicle(car, "03.01.2024", empty_rental), "Should fail as rental system is empty"

    # 8. Client double booking the same vehicle
    rental.rent_vehicle(car, "05.01.2024", client)
    assert not client.book_vehicle(car, "05.01.2024", rental), "Should fail as client has already booked the vehicle"

    print("All edge case tests passed.")

def test_get_sorted_vehicles_list():
    # Initialize the rental system
    rental_system = VehicleRental()

    # Edge Case 1: No vehicles in the system
    assert rental_system.get_sorted_vehicles_list() == [], "Failed on no vehicles in the system"

    # Add vehicles
    car1 = Car(price=100, id="Car1")
    car2 = Car(price=150, id="Car2")
    motorcycle1 = Motorcycle(price=50, id="Bike1")
    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(car2)
    rental_system.add_vehicle(motorcycle1)

    # Edge Case 2: No rentals recorded
    assert rental_system.get_sorted_vehicles_list() == [car2, car1, motorcycle1], \
        "Failed on vehicles with no rentals; should sort by price descending"

    # Simulate rentals
    client = Client(budget=1000)
    rental_system.rent_vehicle(car1, "01.01.2024", client)
    rental_system.rent_vehicle(car1, "02.01.2024", client)  # car1 rented twice
    rental_system.rent_vehicle(car2, "01.01.2024", client)  # car2 rented once

    # Edge Case 3: Rentals exist, check sorting by rental count
    assert rental_system.get_sorted_vehicles_list() == [car1, car2, motorcycle1], \
        "Failed on sorting by rental count"

    # Edge Case 4: Same rental count but different prices
    rental_system.rent_vehicle(motorcycle1, "03.01.2024", client)  # motorcycle1 now rented once
    assert rental_system.get_sorted_vehicles_list() == [car1, car2, motorcycle1], \
        "Failed when same rental count exists; should sort by price descending"

    # Edge Case 5: Vehicles have identical rental count and price
    car3 = Car(price=100, id="Car3")  # Identical price as car1
    rental_system.add_vehicle(car3)
    rental_system.rent_vehicle(car3, "01.01.2024", client)  # car3 rented once
    assert rental_system.get_sorted_vehicles_list() == [car1, car2, car3, motorcycle1], \
        "Failed when vehicles have identical rental counts and prices"

    print("All edge case tests passed!")

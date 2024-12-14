"""Vehicle rental. Project III."""
import enum


class Type(enum.Enum):
    """
    Type of vehicle.

    DO NOT CHANGE.
    """

    SPORTSCAR = 'SPORTSCAR'
    CONVERTIBLE = 'CONVERTIBLE'
    VAN = 'VAN'
    OTHER = 'OTHER'


def get_price(vehicle) -> int:
    """
    Return the price of the vehicle based on its type.

    :param vehicle: A vehicle object (either Car or Motorcycle) with type.

    Motorcycle - 100

    OTHER - 50
    VAN - 100
    CONVERTIBLE - 150
    SPORTSCAR - 200

    :return: Price of the vehicle based on its type.
    """
    if isinstance(vehicle, Motorcycle):
        return 100

    if isinstance(vehicle, Car):
        if vehicle.type_of_car == Type.VAN:
            return 100

        elif vehicle.type_of_car == Type.CONVERTIBLE:
            return 150

        elif vehicle.type_of_car == Type.SPORTSCAR:
            return 200

    return 50


class Car:
    """Car class representing a vehicle of type Car."""

    def __init__(self, make: str, model: str, year: int, type_of_car: Type) -> None:
        """
        Construct new car.

        :param make: Manufacturer of the car.
        :param model: Model of the car.
        :param year: Year the car was manufactured.
        :param type_of_car: Type of the car (an instance of Type enum).
        :raises ValueError: If type_of_car is not an instance of Type enum.
        """
        self.make = make
        self.model = model
        self.year = year
        self.rent_dates = []

        if isinstance(type_of_car, Type):
            self.type_of_car = type_of_car
        else:
            raise ValueError("type_of_car must be an instance of Type enum")

    def __repr__(self) -> str:
        """
        Return string representation of car.

        return: 'Car(make, model, year, type_of_car)'
        """
        return f"Car({self.make}, {self.model}, {self.year}, {self.type_of_car})"

    def __hash__(self) -> int:
        """
        Return hash representation of car.

        return: hash(make, model, year, type_of_car)
        """
        return hash((self.make, self.model, self.year, self.type_of_car))
    
    def __eq__(self, other) -> bool:
        """
        Return equal.

        return: True or False
        """
        if isinstance(other, Car):
            return (
                self.make == other.make
                and self.model == other.model
                and self.year == other.year
                and self.type_of_car == other.type_of_car
            )
        return False

    def get_price(self) -> int:
        """:return: price of the vehicle."""
        return get_price(self)


class Motorcycle:
    """Motorcycle."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Construct new motorcycle.

        :param make: Manufacturer of the motorcycle.
        :param model: Model of the motorcycle.
        :param year: Year the motorcycle was manufactured.
        """
        self.make = make
        self.model = model
        self.year = year
        self.rent_dates = []

    def __repr__(self) -> str:
        """
        Return string representation of Motorcycle.

        return: 'Motorcycle(make, model, year)'
        """
        return f"Motorcycle({self.make}, {self.model}, {self.year})"

    def __hash__(self) -> int:
        """
        Hash representation of Motorcycle.

        return: hash(make, model, year)
        """
        return hash((self.make, self.model, self.year))

    def get_price(self) -> int:
        """:return: price of the vehicle."""
        return get_price(self)


class Client:
    """Client class representing a client of the rental service."""

    def __init__(self, name: str, budget: int) -> None:
        """
        Construct new Client.

        :param name: The name of the client.
        :param budget: The initial budget for the client.
        bookings: A list of vehicles that the client has booked.
        """
        self.name = name
        self.budget = budget
        self.bookings = []
        self.spent = 0

    def book_vehicle(self, vehicle: Car | Motorcycle, date: str, vehicle_rental) -> bool:
        """
        Book a vehicle for a specific date.

        :param vehicle: The vehicle to be booked.
        :param date: The date for the booking.
        :param vehicle_rental: The rental service from which the vehicle is being booked.
        :return: True if the booking is successful, otherwise False.
        """
        if not vehicle or not date or not vehicle_rental:
            return False
        
        if vehicle_rental.rent_vehicle(vehicle, date, self):
            return True
        
        return False


    def total_spent(self) -> int:
        """
        Calculate and return the total amount spent by the client.

        :return: The total amount of money the client has spent on successful bookings.
        """
        return self.spent

    def get_bookings(self) -> list[Car | Motorcycle]:
        """:return: List of all the vehicles client has booked."""
        return self.bookings


class VehicleRental:
    """Vehicle rental system managing vehicles, rents and budget."""

    def __init__(self) -> None:
        """Construct new VehicleRental."""
        self.clients = []
        self.booked_cars = {}
        self.balance = 0

    def get_money(self) -> int:
        """
        Return the account balance VehicleRental currently has.

        :return: amount money that rental system has.
        """
        return self.balance

    def get_motorcycles(self) -> list[Motorcycle]:
        """:return: list of motorcycles in rental system."""
        return list(filter(lambda vehicle: isinstance(vehicle, Motorcycle), self.booked_cars.keys()))

    def get_cars(self) -> list[Car]:
        """:return: list of cars in rental system."""
        return list(filter(lambda vehicle: isinstance(vehicle, Car), self.booked_cars.keys()))

    def get_vehicle_bookings_dict(self) -> dict[Car | Motorcycle, list[str]]:
        """
        Get a dictionary of vehicles and their booked dates.

        This method returns a dictionary where the keys are vehicle objects (either `Car` or `Motorcycle`)
        and the values are lists of dates when the vehicles have been booked.

        Example:
            {
                Car(Ford, Sierra, 1993, Type.SPORTSCAR): ["23.12.2024", "21.01.2025"],
                Motorcycle(Ducati, Panigale, 2014): ["23.12.2024", "21.01.2025"]
            }

        :return: dictionary with vehicles as keys and lists of booked dates as values.
        """
        return self.booked_cars

    def get_clients(self) -> list[Client]:
        """:return: list of all clients who have placed a booking in rental."""
        return self.clients

    def add_vehicle(self, vehicle: Car | Motorcycle) -> bool:
        """
        Add a vehicle to the rental system if it is not already present.

        If vehicle with same hash is present it must not be added to the VehicleRental, return False.

        :param vehicle: Vehicle (Car or Motorcycle) to be added.
        :return: True if the vehicle was successfully added, False if it was already present.
        """
        if vehicle not in self.booked_cars:
            self.booked_cars[vehicle] = []
            return True
        return False

    def is_vehicle_available(self, vehicle: Car | Motorcycle, date: str) -> bool:
        """
        Check if the vehicle is available for rent on the specified date.

        :param vehicle: The vehicle to check availability for.
        :param date: The date to check availability on.
        :return: True if the vehicle is available, otherwise False.
        """
        return date not in vehicle.rent_dates

    def rent_vehicle(self, vehicle: Car | Motorcycle, date: str, client: Client) -> bool:
        """
        Rent a vehicle to a client for a specified date if it is available and the client has sufficient funds.

        If booking the vehicle was successful, increase the budget of the rental.

        Vehicle, date and client must not be empty or None.

        :param vehicle: Vehicle to be rented.
        :param date: Date for which the vehicle is being rented.
        :param client: Client who is renting the vehicle.
        :return: True if the rental was successful, otherwise False.
        """
        if not vehicle or not date or not client:
            return False
        
        if vehicle not in self.booked_cars or date in self.booked_cars[vehicle]:
            return False
        
        price = vehicle.get_price()
        if client.budget < price:
            return False
        
        if vehicle not in self.booked_cars:
            self.booked_cars[vehicle] = []

        client.budget -= price
        self.balance += price
        self.booked_cars[vehicle].append(date)
        client.bookings.append(vehicle)
        vehicle.rent_dates.append(date)
        return True

    def get_most_rented_vehicle(self) -> list[Motorcycle | Car]:
        """
        Return the most rented vehicle(s) from the rental system.

        :return: A list of the most rented vehicles, list could contain only one vehicle. If multiple vehicles have been
         rented the same number of times, all of those are returned. If no vehicle have been rented, return an empty
         list.
        """
        if not self.booked_cars:
            return []

        non_empty_bookings = {vehicle: dates for vehicle, dates in self.booked_cars.items() if dates}

        if not non_empty_bookings:
            return []

        most_rented_count = max(len(dates) for dates in non_empty_bookings.values())
        most_rented_vehicles = [vehicle for vehicle, dates in non_empty_bookings.items() if len(dates) == most_rented_count]

        return most_rented_vehicles

    def find_vehicle_by_make(self, make: str) -> list[Car | Motorcycle]:
        """
        Find vehicles by their manufacturer (make).

        :param make: Manufacturer to search for (case-insensitive).
        :return: A list of vehicles matching the given make.
        """
        make = make.lower()
        return [vehicle for vehicle in self.booked_cars.keys() if vehicle.make.lower() == make]

    def find_car_by_type(self, type_of_car: Type) -> list[Car]:
        """
        Find cars by their type (e.g., SPORTSCAR, VAN, etc.).

        :param type_of_car: The type of car to search for (an instance of Type enum).
        :return: A list of cars matching the given type.
        """
        return [vehicle for vehicle in self.booked_cars.keys() if isinstance(vehicle, Car) and vehicle.type_of_car == type_of_car]

    def get_best_client(self) -> Client:
        """
        Return the best client who rented the most vehicles.

        If multiple clients have rented the same number of vehicles, return the client who spent the most money.
        :return: The best client object.
        """
        checked_clients = []

        for client in self.clients:
            if client.bookings:
                checked_clients.append(client)
        
        if not checked_clients:
            return None

        return max(checked_clients, key=lambda client: (len(client.bookings), client.total_spent()))

    def get_sorted_vehicles_list(self) -> list[Car | Motorcycle]:
        """
        Return a list of vehicles sorted from most rented to least rented.

        In case of a tie, vehicles are sorted by price from highest to lowest.
        :return: A list of vehicles sorted by popularity and price.
        """
        return sorted(self.booked_cars.keys(), key=lambda vehicle: (len(self.booked_cars[vehicle]), vehicle.get_price()), reverse=True)

    def get_vehicles_by_year_range(self, start_year: int, end_year: int) -> list[Car | Motorcycle]:
        """
        Return a list of vehicles manufactured within a specified year range.

        :param start_year: The start year of the range (inclusive).
        :param end_year: The end year of the range (inclusive).
        :return: A list of vehicles manufactured within the specified year range.
        :raises ValueError: If start_year or end_year are not integers or if start_year > end_year.
        """
        if not isinstance(start_year, int) or not isinstance(end_year, int):
            raise ValueError("Start and end years must be integers")

        if start_year > end_year:
            raise ValueError("Start year must be less than or equal to end year")

        return [vehicle for vehicle in self.booked_cars.keys() if start_year <= vehicle.year <= end_year]

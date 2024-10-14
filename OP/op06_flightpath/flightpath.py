"""Flightpath."""


def update_delayed_flight(schedule: dict[str, tuple[str, str]], delayed_flight_number: str, new_departure_time: str) -> \
        dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the departure time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    output = {}
    for flight in schedule:
        if schedule[flight][1] == delayed_flight_number:
            output[new_departure_time] = schedule[flight]
        else:
            output[flight] = schedule[flight]

    return output


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    output = {}
    for flight in schedule:
        if schedule[flight][1] == cancelled_flight_number:
            continue
        else:
            output[flight] = schedule[flight]

    return output


def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    The busiest hour(s) is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    hours = {}
    for time in schedule:
        time_hour = time.split(":")[0]
        if time_hour in hours:
            hours[time_hour] += 1
        else:
            hours[time_hour] = 1
    max_value = max(hours.values())

    return [hour for hour in hours if hours[hour] == max_value]


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    output = []
    for time in schedule:
        incoming_flight_minutes = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        outgoing_flight_minutes = int(arrival[0].split(":")[0]) * 60 + int(arrival[0].split(":")[1])

        if 45 < incoming_flight_minutes - outgoing_flight_minutes < 240 and schedule[time][0] != arrival[1]:
            output += [(time, schedule[time][0])]
    return output


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    if schedule == {}:
        return []
    output = {}
    if len(schedule) == 1:
        return [list(schedule.keys())[0]]
    for start_time in schedule:
        start_time_min = int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1])
        for current_time in schedule:
            current_time_min = int(current_time.split(":")[0]) * 60 + int(current_time.split(":")[1])
            if 0 < current_time_min - start_time_min < 60:
                if start_time in output:
                    output[start_time] += 1
                else:
                    output[start_time] = 1
    max_value = max(output.values())
    return [time for time in output if output[time] == max_value]

def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    output = {}
    for time in schedule:
        flight_dest = schedule[time][0]
        flight_number = schedule[time][1]
        flight_count = passenger_count[flight_number]
        if flight_dest in output:
            output[flight_dest] += flight_count
        else:
            output[flight_dest] = flight_count
    return max(output, key= lambda x: output[x])
        

def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    output = {}
    for time in schedule:
        flight_dest = schedule[time][0]
        flight_number = schedule[time][1]
        flight_count = passenger_count[flight_number]
        if flight_dest in output:
            output[flight_dest] += flight_count
        else:
            output[flight_dest] = flight_count
    return min(output, key= lambda x: output[x])


if __name__ == '__main__':
    flight_schedule = {
        "06:15": ("Tallinn", "OWL6754"),
        "11:35": ("Helsinki", "BHM2345")
    }
    new_flight_schedule = update_delayed_flight(flight_schedule, "OWL6754", "09:00")
    print(flight_schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_flight_schedule)
    # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    new_flight_schedule = cancel_flight(flight_schedule, "OWL6754")
    print(flight_schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_flight_schedule)
    # {'11:35': ('Helsinki', 'BHM2345')}

    flight_schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }
    print(busiest_time(flight_schedule))
    # ['06', '11']

    print(connecting_flights(flight_schedule, ("04:00", "Tallinn")))
    # [('06:30', 'Paris'), ('07:29', 'London')]
    
    schedule = {
    "08:00": ("Paris", "OWL1234"),
    "08:15": ("London", "BHM5678"),
    "08:45": ("Berlin", "NIN9012"),
    "15:20": ("Tallinn", "BHM2134"),
    "15:45": ("Tokyo", "NIN2342")
    }
    print(busiest_hour(schedule))
    # ["08:00"]
    
    schedule = {
        "08:00": ("Paris", "OWL1234"),
        "08:15": ("London", "BHM5678"),
        "08:45": ("Berlin", "NIN9012"),
        "09:00": ("Helsinki", "OWL2345"),
        "09:15": ("Oslo", "FLP7654"),
        "15:20": ("Tallinn", "BHM2134"),
        "15:45": ("Tokyo", "NIN2342"),
        "16:15": ("Dublin", "TRE4567"),
    }
    print(busiest_hour(schedule))
    # ["08:00", "08:15", "08:45", "15:20"]
    
    schedule = {
        "08:00": ("Paris", "OWL1234"),
    }
    print(busiest_hour(schedule))
    # ['08:00']
    
    
    # flight number: number of passengers
    passenger_counts = {
        "MWL6754": 100,
        "OWL6754": 85,
        "OWL6751": 103,
        "OWL6756": 87,
        "OWL6759": 118,
        "OWL6752": 90,
        "BHM2345": 111,
        "BHM2346": 102,
        "BHM2347": 94,
        "TLN1001": 1
    }
    print(most_popular_destination(flight_schedule, passenger_counts))
    # Paris

    print(least_popular_destination(flight_schedule, passenger_counts))
    # Tallinn

"""Mama's donuteria."""
import math


class Donut:
    """Donut class."""

    def __init__(self, name: str, price: float, ingredients: list, allergies: list):
        """
        Initialize a donut object.

        :param name: The name of the donut.
        :param price: The price of the donut.
        :param ingredients: Ingredients.
        :param allergies: Allergies.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.allergies = allergies

    def __repr__(self):
        """Return a string representation of the Donut object."""
        return f"{self.name}, {self.price}, {self.ingredients}, {self.allergies}"


def sort_donuts_by_price(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts by their price in ascending order.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted by price.
    """
    return list(map(lambda donut: donut.name, sorted(donut_list, key=lambda donut: donut.price)))


def find_least_expensive_donut(donut_list: list[Donut]) -> str:
    """
    Find the name of the least expensive donut.

    :param donut_list: List of Donut objects.
    :return: Name of the least expensive donut.
    """
    return min(donut_list, key=lambda donut: donut.price).name


def find_donuts_with_ingredient(donut_list: list[Donut], ingredient: str) -> list[str]:
    """
    Find donuts that contain a specific ingredient.

    :param donut_list: List of Donut objects.
    :param ingredient: Ingredient that donut must contain.
    :return: List of Donut names containing the specified ingredient.
    """
    return list(map(lambda donut: donut.name, list(filter(lambda donut: ingredient in donut.ingredients, donut_list))))


def list_donut_names_and_ingredients(donut_list: list[Donut]) -> list[dict]:
    """
    Create a list containing the names and ingredients of donuts.

    :param donut_list: List of donut objects.
    :return: List of dictionaries containing donut names and ingredients.
    """
    return list(map(lambda donut: {donut.name: donut.ingredients}, donut_list))


def list_donuts_starting_with(donut_list: list[Donut], letter: str) -> list[str]:
    """
    Find donuts whose names start with a specific letter and sort them alphabetically.

    :param donut_list: List of Donut objects.
    :param letter: The starting letter to filter donut names by.
    :return: List of Donut names sorted alphabetically.
    """
    return sorted(map(lambda donut: donut.name, list(filter(lambda donut: donut.name.lower().startswith(letter.lower()), donut_list))))


def find_flour_needed_for_baking(donut_list: list[Donut], quantity: int) -> int:
    """
    Calculate the amount of flour needed to bake a certain quantity of each donut.

    Bakery needs 80 grams of flour multiply by donut price to bake one.

    :param donut_list: List of Donut objects.
    :param quantity: The quantity of each donut to be baked.
    :return: Total amount of flour needed in grams rounded up.
    """
    return math.ceil(sum(map(lambda donut: quantity * 80 * donut.price, donut_list)))


def calculate_tip(donut_list: list[Donut], customers: int) -> int:
    """
    Calculate the tip amount that will be left.

    Every customer visiting bakery will buy one of each sugar containing donuts and leave 20% tip.

    :param donut_list: List of Donut objects.
    :param customers: Number of customers visiting bakery.
    :return: Tip amount.
    """
    return math.floor(sum(map(lambda donut: customers * donut.price * 0.2, list(filter(lambda donut: "sugar" in donut.ingredients, donut_list)))))


def sort_donuts_by_allergies(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts by the number of allergies they contain.

    The more allergies the higher on the list.
    In case of a tie sort alphabetically by donut name.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted by allergies and then alphabetically.
    """
    return list(map(lambda donut: donut.name, sorted(donut_list, key=lambda donut: (-len(donut.allergies), donut.name))))


def calculate_profit_per_day(donut_list: list[Donut], quantity_per_day: int, cost_per_donut: float) -> int:
    """
    Calculate profit per day for selling a certain quantity of each donut.

    :param donut_list: List of Donut objects.
    :param quantity_per_day: The quantity of each donut sold per day.
    :param cost_per_donut: The cost to make each donut.
    :return: Profit per day rounded down.
    """
    return math.floor(sum(map(lambda donut: quantity_per_day * (donut.price - cost_per_donut), donut_list)))


def find_most_popular_donut(donut_list: list[Donut]) -> str:
    """
    Find the most popular donut based on the number of allergies (fewer allergies are more popular).

    In case of a tie the most popular donut is with lower price.

    :param donut_list: List of Donut objects.
    :return: The name of the most popular donut.
    """
    return min(donut_list, key=lambda donut: (len(donut.allergies), donut.price)).name


def sort_donuts_alphabetically_by_name(donut_list: list[Donut]) -> list[str]:
    """
    Sort donuts alphabetically by name.

    :param donut_list: List of Donut objects.
    :return: List of Donut names sorted alphabetically.
    """
    return list(map(lambda donut: donut.name, sorted(donut_list, key=lambda donut: donut.name)))


def find_donuts_costing_more_than(donut_list: list[Donut], price_threshold: float) -> list[str]:
    """
    Find donuts that cost more than a specified price.

    :param donut_list: List of Donut objects.
    :param price_threshold: The minimum price threshold.
    :return: List of Donut names that cost more than the specified threshold.
    """
    return list(map(lambda donut: donut.name, filter(lambda donut: donut.price > price_threshold, donut_list)))


def find_donuts_with_no_allergy(donut_list: list[Donut], allergy: str) -> list[str]:
    """
    Find donuts with no occurrence of a specific allergy.

    :param donut_list: List of Donut objects.
    :param allergy: The allergy to exclude.
    :return: List of Donut names with no occurrence of the specified allergy.
    """
    return list(map(lambda donut: donut.name, filter(lambda donut: allergy not in donut.allergies, donut_list)))

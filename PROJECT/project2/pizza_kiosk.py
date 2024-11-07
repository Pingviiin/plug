"""Pizza making."""
import re


def is_correct_name(ingredient: str) -> bool:
    """Check if ingredient name is correct.

    Args:
        ingredient (str): Name of the ingredient

    Returns:
        bool: True if correct name, False if incorrect
    """
    if ingredient == "":
        return False

    for i in ingredient:
        if i.islower():
            continue
        else:
            return False
    else:
        return True


def fix_names(ingredients: list) -> list:
    """Fix the names of ingredients in a list.

    Args:
        ingredients (list): Strings

    Returns:
        list: A list of correct ingredient names
    """
    output = []

    for ingredient in ingredients:
        if ingredient == "":
            continue

        if is_correct_name(ingredient):
            output.append(ingredient)
            continue

        str_output = ""

        for i in ingredient:
            if i.islower():
                str_output += i
            elif i.isupper():
                str_output += i.lower()
        output.append(str_output)

    return output


def pizza_at_index(pizzas: list, pizza: str) -> str:
    """Find pizza at index, which is a count of how many of one specific pizza are in the list.

    Args:
        pizzas (list): List of pizzas
        pizza (str): Pizza, which will be indexed

    Returns:
        str: Name of pizza, which is at the index
    """
    index = pizzas.count(pizza)

    if index >= len(pizzas):
        return ""

    else:
        return pizzas[index]


def format_orders(nr_order: list) -> dict:
    """Format orders from a list of string into a dictionary.

    Args:
        nr_order (list): List of strings

    Returns:
        dict: Correctly formatted order
    """
    output = {}

    for order in nr_order:
        order = order.split("&")
        output[int(order[0])] = order[1].lower()

    return output


def calculate_income(prices: str) -> float:
    """Calculate daily income.

    Args:
        prices (str): String which contains numbers with random symbols inbetween

    Returns:
        float: Sum of daily income
    """
    if len(prices) < 5:
        return 0.0

    match = re.match(r'(\d{2}\.\d{2})', prices)

    if match:
        price = float(match.group(1))
        return price + calculate_income(prices[match.end():])

    else:
        return calculate_income(prices[1:])


def switch_keys_and_values(pizza_orders: dict) -> dict:
    """Switch the keys and values in a dictionary.

    Args:
        pizza_orders (dict): Dictionary with pizza orders

    Returns:
        dict: Dictionary with counts of specific pizzas
    """
    output = {}

    for pizza, nums in pizza_orders.items():

        for i in nums:
            if i not in output:
                output[i] = [pizza]
            else:
                output[i] += [pizza]

    return output


def count_ingredients(menu: dict, order: list) -> dict | None:
    """Count ingredients needed to make multiple pizzas.

    Args:
        menu (dict): Dictionary of all the valid pizzas
        order (list): List of pizzas which require ingredients

    Returns:
        dict | None: Dictionary of required ingredients to make pizzas in a order
    """
    output = {}

    for pizza in order:
        if pizza not in menu:
            return {}

        for ingredient in menu[pizza]:
            if ingredient not in output:
                output[ingredient] = 1
            else:
                output[ingredient] += 1

    return output


def match_pizzas_with_prices(pizzas: list, prices: list) -> list:
    """Match pizzas with prices.

    Args:
        pizzas (list): List of pizzas
        prices (list): List of prices

    Returns:
        list: List of pizzas with matching prices
    """
    unique_pizzas = []
    duplicates = set()
    pattern = re.compile(r"^[a-z]+$")

    for pizza in pizzas:
        if pattern.match(pizza) and pizza not in duplicates:
            unique_pizzas.append(pizza)
            duplicates.add(pizza)

    if len(prices) != len(unique_pizzas):
        return []

    else:
        return list(zip(unique_pizzas, prices))

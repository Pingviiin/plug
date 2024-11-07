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
    index = pizzas.count(pizza) - 1

    if index == 0:
        return ""

    if index < len(pizzas):
        return pizzas[index]
    
    else:
        return ""


def format_orders(nr_order: list) -> dict:
    output = {}

    for order in nr_order:
        order = order.split("&")
        output[int(order[0])] = order[1].lower()

    return output


def calculate_income(prices: str) -> float:
    if len(prices) < 5:
        return 0.0

    match = re.match(r'(\d{2}\.\d{2})', prices)

    if match:
        price = float(match.group(1))
        return price + calculate_income(prices[match.end():])

    else:
        return calculate_income(prices[1:])


def switch_keys_and_values(pizza_orders: dict) -> dict:
    output = {}

    for pizza, nums in pizza_orders.items():

        for i in nums:
            if i not in output:
                output[i] = [pizza]
            else:
                output[i] += [pizza]

    return output


def count_ingredients(menu: dict, order: list) -> dict | None:
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


# Test case 1: Basic functionality with the target pizza at a valid index
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa") == "kanapitsa", "Test case 1 failed"

# Test case 2: Multiple occurrences of the target pizza, with the resulting index within range
assert pizza_at_index(["juustupitsa", "pepperoni", "juustupitsa", "kanapitsa", "juustupitsa"], "juustupitsa") == "kanapitsa", "Test case 2 failed"

# Test case 3: Target pizza does not exist in the list (should return an empty string)
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "hawaii") == "", "Test case 3 failed"

# Test case 4: Only one occurrence of the target pizza, and it's the last element
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "pepperoni") == "kanapitsa", "Test case 4 failed"

# Test case 5: The target pizza count matches an out-of-range index
assert pizza_at_index(["juustupitsa", "pepperoni"], "juustupitsa") == "pepperoni", "Test case 5 failed"  # Index 1 is out of range

# Test case 6: Target pizza occurs multiple times, but the resulting index is valid
assert pizza_at_index(["juustupitsa", "juustupitsa", "juustupitsa"], "juustupitsa") == "", "Test case 6 failed"  # Index 3 is valid

# Test case 7: Empty list (should return an empty string)
assert pizza_at_index([], "pepperoni") == "", "Test case 7 failed"

# Test case 8: Single-element list, where the target pizza does not exist
assert pizza_at_index(["juustupitsa"], "pepperoni") == "", "Test case 8 failed"

# Test case 9: Single-element list, where the target pizza exists
assert pizza_at_index(["pepperoni"], "pepperoni") == "", "Test case 9 failed"  # Index 1 is out of range

# Test case 10: Multiple types of pizzas with varying counts
assert pizza_at_index(["pepperoni", "juustupitsa", "kanapitsa", "juustupitsa", "pepperoni", "juustupitsa"], "pepperoni") == "kanapitsa", "Test case 10 failed"

print("All test cases passed!")

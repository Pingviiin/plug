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
    pizzas = fix_names(pizzas)
    index = pizzas.count(pizza)
    if index == 0:
        return ""
    elif index >= len(pizzas):
        return ""
    else:
        return pizzas[index]


def format_orders(nr_order: list) -> dict:
    output = {}
    for order in nr_order:
        order = order.split("&")
        output[int(order[0])] = order[1].lower()
    return output


def calculate_income(prices: str) -> float:
    prices = re.findall(r'(\d{2}\.\d{2})', prices)

    def price_total(prices, total):
        if not prices:
            return total
        else:
            return price_total(prices[1:], total + float(prices[0]))

    return price_total(prices, 0.0)


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
        if pizza not in list(menu.keys()):
            continue
        for ingredient in menu[pizza]:
            if ingredient not in output:
                output[ingredient] = 1
            else:
                output[ingredient] += 1
    return output


def match_pizzas_with_prices(pizzas: list, prices: list) -> list:
    pizzas = fix_names(pizzas)
    unique_pizzas = []
    output = []

    [unique_pizzas.append(i) for i in pizzas if i not in unique_pizzas]

    for i, pizza in enumerate(unique_pizzas):
        output += [(pizza, prices[i])]

    return output


print(is_correct_name("banana"))
print(is_correct_name("Banana"))
print(is_correct_name("12412Banana"))
print(is_correct_name("PINEAPPLE--."))
print(fix_names(["banana", "BANANA", ""]))
print(fix_names(["2423dsfsdf", ".dfgdgffdg...."]))
print(pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa"))
print(pizza_at_index(["pepperoni", "juustupitsa", "kanapitsa", "juustupitsa", "bbq"], "juustupitsa"))
print(pizza_at_index(["pepperoni"], "pepperoni"))
print(pizza_at_index(["pepperoni", "kanapitsa", "bbq"], "juustupitsa"))
print(format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]))
print(calculate_income("15.03*05.99|)=01.20&.$50.37"))
print(calculate_income(""))
print(switch_keys_and_values({"kanapitsa": [1, 5, 3, 4], "juustupitsa": [1, 2], "pepperoni": [1, 5, 3]}))
print(count_ingredients({"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]}, ["margarita", "margarita", "pepperoni"]))
print(match_pizzas_with_prices(["pepperoni", "margarita", "ch7eese", "cheese", "margarita"], [3.99, 4.99, 3.99]))

# Test case 1: Basic functionality with multiple pizzas in the order
assert count_ingredients(
    {"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]},
    ["margarita", "margarita", "pepperoni"]
) == {"juust": 3, "kaste": 3, "tomat": 2, "pepperoni": 1}, "Test case 1 failed"

# Test case 2: Order with only one type of pizza
assert count_ingredients(
    {"margarita": ["juust", "tomat", "kaste"]},
    ["margarita", "margarita"]
) == {"juust": 2, "tomat": 2, "kaste": 2}, "Test case 2 failed"


# Test case 4: Order list is empty (no pizzas ordered)
assert count_ingredients(
    {"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]},
    []
) == {}, "Test case 4 failed"  # Should return an empty dictionary

# Test case 5: Menu has multiple pizzas, but order only includes pizzas with unique ingredients
assert count_ingredients(
    {"veggie": ["juust", "tomat", "sibul"], "meat_lovers": ["kaste", "liha", "juust"]},
    ["veggie", "meat_lovers"]
) == {"juust": 2, "tomat": 1, "sibul": 1, "kaste": 1, "liha": 1}, "Test case 5 failed"

# Test case 6: Menu has pizzas with the same ingredients, ordered multiple times
assert count_ingredients(
    {"margarita": ["juust", "tomat", "kaste"], "extra_cheese": ["juust", "juust", "kaste"]},
    ["margarita", "extra_cheese", "extra_cheese"]
) == {"juust": 5, "tomat": 1, "kaste": 3}, "Test case 6 failed"

# Test case 7: Menu contains no pizzas (empty menu)
assert count_ingredients({}, ["margarita", "pepperoni"]) == {}, "Test case 7 failed"

# Test case 8: All pizzas ordered are available in menu with duplicate ingredients
assert count_ingredients(
    {"double_cheese": ["juust", "juust", "tomat"], "pepperoni": ["juust", "kaste", "pepperoni"]},
    ["double_cheese", "pepperoni", "double_cheese"]
) == {"juust": 5, "tomat": 2, "kaste": 1, "pepperoni": 1}, "Test case 8 failed"

print("All test cases passed!")

# Test case 1: Basic functionality with multiple orders
assert format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]) == {5: "kanapitsa", 1: "pepperoni", 20: "mexican"}, "Test case 1 failed"

# Test case 2: Single order
assert format_orders(["10&margherita"]) == {10: "margherita"}, "Test case 2 failed"

# Test case 3: Orders with mixed case order names
assert format_orders(["2&HAWAII", "3&cheesE", "4&VeGGiE"]) == {2: "hawaii", 3: "cheese", 4: "veggie"}, "Test case 3 failed"

# Test case 4: Orders with large order numbers
assert format_orders(["1000&pepperoni", "500&bbq"]) == {1000: "pepperoni", 500: "bbq"}, "Test case 4 failed"

# Test case 5: Empty input list
assert format_orders([]) == {}, "Test case 5 failed"  # Should return an empty dictionary

# Test case 6: Orders with similar names but different numbers
assert format_orders(["1&veggie", "2&VEGGIE", "3&Veggie"]) == {1: "veggie", 2: "veggie", 3: "veggie"}, "Test case 6 failed"

# Test case 7: Orders with special characters in order names
assert format_orders(["5&chicken-pizza", "7&bbq_ribs", "9&veggie deluxe"]) == {5: "chicken-pizza", 7: "bbq_ribs", 9: "veggie deluxe"}, "Test case 7 failed"

# Test case 8: Leading and trailing whitespace in order name
#assert format_orders(["10&  Margherita ", "11&PePPeroni "]) == {10: "margherita", 11: "pepperoni"}, "Test case 8 failed"

# Test case 9: Edge case with very large number as order number
assert format_orders(["999999999&supreme"]) == {999999999: "supreme"}, "Test case 9 failed"

# Test case 10: Multiple orders with different formats to confirm order is preserved
assert format_orders(["3&margherita", "1&pepperoni", "2&hawaiian"]) == {3: "margherita", 1: "pepperoni", 2: "hawaiian"}, "Test case 10 failed"

print("All test cases passed!")

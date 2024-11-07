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

    if index >= len(pizzas) or index == 0:
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

# Test case 3: Order with a pizza that is not on the menu
assert count_ingredients(
    {"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]},
    ["margarita", "hawaii"]
) == {}, "Test case 3 failed"  # Should return an empty dictionary

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


# Test case 1: Basic functionality with the target pizza at a valid index
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa") == "kanapitsa", "Test case 1 failed"

# Test case 2: Multiple occurrences of the target pizza, with the resulting index within range
assert pizza_at_index(["juustupitsa", "pepperoni", "juustupitsa", "kanapitsa", "juustupitsa"], "juustupitsa") == "kanapitsa", "Test case 2 failed"

# Test case 3: Target pizza does not exist in the list (should return an empty string)
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "hawaii") == "", "Test case 3 failed"

# Test case 4: Only one occurrence of the target pizza, and it's the last element
assert pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "pepperoni") == "kanapitsa", "Test case 4 failed"

# Test case 5: The target pizza count matches an out-of-range index
assert pizza_at_index(["juustupitsa", "pepperoni"], "juustupitsa") == "pepperoni", "Test case 5 failed"

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


# Test case 1: Basic functionality with mixed delimiters
assert calculate_income("15.03*05.99|)=01.20&.$50.37") == 72.59, "Test case 1 failed"

# Test case 2: Only prices with different delimiters
assert calculate_income("10.00|20.50&30.00") == 60.50, "Test case 2 failed"

# Test case 3: Single price without delimiters
assert calculate_income("15.99") == 15.99, "Test case 3 failed"

# Test case 4: Multiple prices with unusual symbols between them
assert calculate_income("99.99*&^#20.01$$$45.50") == 165.50, "Test case 4 failed"

# Test case 5: No valid prices (should return 0.0)
assert calculate_income("&^#%@$$$") == 0.0, "Test case 5 failed"

# Test case 6: Prices with unusual spacing
assert calculate_income("    05.55**07.25 !! 12.00%%") == 24.80, "Test case 6 failed"

# Test case 7: Edge case with price at start and end
assert calculate_income("30.00hello45.25goodbye60.75") == 136.00, "Test case 7 failed"

# Test case 8: Large input with repeated prices
assert calculate_income("10.00|") == 10.00, "Test case 8 failed"  # Should correctly sum up repeated prices

# Test case 9: Mixed decimal points and non-price dot occurrences
assert calculate_income("15.03extra.text99.99dots15.99") == 131.01, "Test case 9 failed"

# Test case 10: Prices with special characters but valid pattern
assert calculate_income("*20.40*random*text*10.10*50.50*") == 81.00, "Test case 10 failed"

print("All test cases passed!")

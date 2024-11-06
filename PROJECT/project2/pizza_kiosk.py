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
    if index >= len(pizzas):
        return ""
    else:
        return pizzas[index]


def format_orders(nr_order: list) -> dict:
    output = {}
    for order in nr_order:
        order = order.split("&")
        output[order[0]] = order[1].lower()
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
        for ingredient in menu[pizza]:
            if ingredient not in output:
                output[ingredient] = 1
            else:
                output[ingredient] += 1
    return dict(sorted(output.items(), key=lambda i: i[1], reverse=True))


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
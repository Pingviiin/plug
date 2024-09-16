"""Phone inventory vol 2."""
def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    if len(all_phones) == 0:
        return []

    return all_phones.split(",")


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    """
    phones = list_of_phones(all_phones)
    brands = []

    if len(all_phones) == 0:
        return []

    for i in phones:
        i = i.split(" ")

        if i[0] in brands:
            continue

        brands.append(i[0])

    return brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    phones = list_of_phones(all_phones)
    brands = phone_brands(all_phones)
    models = []

    if len(all_phones) == 0:
        return []

    for i in phones:
        i = i.split(" ")

        for e in brands:
            if i[0] == e:
                i.pop(0)

        i = " ".join(i)
        if i in models:
            continue

        models.append(i)

    return models


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    phones = list_of_phones(all_phones)
    results = []

    for i in phones:
        i = i.split(" ")

        for x in i:
            if brand.lower().count(x.lower()) > 0:
                results.append(" ".join(i))
                break

    return results


def add_phone_quantity(phone_info: tuple, update: tuple) -> tuple:
    """
    Update tuple, if updated data brand and model exist.

    Given a tuple containing a phone brand, its models, and quantities,
    and an update tuple, return the updated data or empty tuple if brand and/or model doesn't exist.
    """
    if phone_info[0] != update[0]:
        return ()

    inventory = []
    for i in phone_info[1]:

        if i == update[1]:
            inventory = list(phone_info[2])
            inventory[phone_info[1].index(i)] += update[2]

    output = (phone_info[0], phone_info[1], tuple(inventory))
    return output


def highest_quantity_brand(phones: list[tuple]) -> str:
    """
    Find brand with most models.

    Given a tuple containing phone brand data, return the brand with the highest total quantity of models.
    If there is a tie, return the one that appears first in the input list.
    """
    name = ""
    summa = 0
    result_list = []
    
    
    for i in range(0, len(phones)):
        name = phones[i][0]
        summa = sum(phones[i][2])
        result = (name, summa)
        result_list.append(result)
    
    if result_list == []:
        return ""
    return max(result_list, key= lambda x: x[1])[0]


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    """
    string = ""

    for list1 in phone_list:
        for model in list1[1]:
            string += f"{list1[0]} {model},"
            
    return string.rstrip(",")

if __name__ == '__main__':
    print(add_phone_quantity(("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                              ("Apple", "iPhone 11", 1)))
    # ("Apple", ["iPhone 11", "iPhone 12"], (501, 300))

    print(add_phone_quantity(
        ("Apple", ["iPhone 11", "iPhone 12"], (500, 300)), ("Nokia", "3310", 10)))
    # ()

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                                  ("Samsung", ["Galaxy S20",
                                   "Galaxy S21"], (600, 400)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (200, 100))]))
    # Samsung

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (100, 50)),
                                  ("Samsung", ["Galaxy S20",
                                   "Galaxy S21"], (110, 40)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (70, 30))]))
    # Apple

    print(phone_list_as_string([['IPhone', ['11', "12"]], ['Google', ['Pixel']]]))
    # IPhone 11, IPhone 12, Google Pixel
    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))
    # IPhone 11,Google Pixel
    print(phone_list_as_string([['HTC', ['one']]]))
    # HTC one
    
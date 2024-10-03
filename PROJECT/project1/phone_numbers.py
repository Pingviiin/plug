"""
Phone number checker.

Siia koodi on ohverdatud vähemalt 6 vabatahtlikku last, kelle otsus ei olnud kindlasti mitte mõjutatud väliste faktorite poolt.
"""


def add_country_code(number: str) -> str:
    """Add country code infront of phone number.
    If a phone number already has a country code return it.

    Args:
        number (str): A phone number

    Returns:
        str: A phone number with a country code
    """
    if number.startswith("+"):
        return number
    else:
        return "+372 " + number


def is_valid(number: str) -> bool:
    """Check if a phone number is correctly formatted.

    Args:
        number (str): A phone number

    Returns:
        bool: True if correctly formatted, False if not
    """
    if number.startswith("+"):

        if number[1].isdigit():

            if number[1:6].count(" ") == 1:

                num_without_cc = number.split(" ")[1]
                if len(num_without_cc) >= 7:

                    num_without_space = number.replace(" ", "")
                    if num_without_space[1:].isdigit():
                        return True
    return False


def remove_unnecessary_chars(number: str) -> str:
    """Remove everything except for the country code and phone number.

    Args:
        number (str): A phone number

    Returns:
        str: A filtered phone number with or without a country code.
    """
    output_num = ""
    fnum_index = -1

    # võtame kõik prügi ära
    num = list(filter(lambda x: x.isdigit() or x == " ", number))
    num = "".join(num)
    num = num.strip()

    # berliini müür
    cc = num.split(" ", 1)[0]
    cc = "".join(list(filter(lambda x: x.isdigit(), cc)))

    # kui numbris on rohkem kui üks tühik siis paneme numbrid ühte kambrisse
    if len(num.split(" ", 1)) > 1:
        output_num = num.split(" ", 1)[1]
        output_num = "".join(list(filter(lambda x: x.isdigit(), output_num)))

    # kus küll peitub esimene number?
    for i, char in enumerate(number):
        if char.isdigit():
            fnum_index = i - 1
            break

    # kui + pole või on enne esimest numbrit
    if fnum_index < number.find("+") or number.count("+") == 0:
        return cc + output_num

    # kui number või maakood on on puudu siis cancel
    elif len(cc) > 0 and len(output_num) > 0:
        return f"+{cc} {output_num}"

    else:
        return cc + output_num


def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    """Get the n amount of numbers from a list of phone numbers.

    Args:
        numbers (list[str]): List of phone numbers
        n (int): Amount of phone numbers

    Returns:
        list[str]: _description_
    """
    if n > len(numbers):
        return numbers
    if n <= 0:
        return []
    return numbers[-n::]


def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    """Get the first correct number from a contact list.

    Args:
        names (list[str]): List of contact names
        numbers (list[str]): List of phone numbers
        name (str): Contact name which needs to match a phone number

    Returns:
        str | None: No contact with such name is found
    """
    for i in range(len(names)):
        if name.lower() == names[i].lower():
            if is_valid(numbers[i]):
                return numbers[i]


def correct_numbers(numbers: list[str]) -> list[str]:
    """Filter correct numbers from a list if possible.

    Args:
        numbers (list[str]): List of phone numbers.

    Returns:
        list[str]: List of correctly formatted phone numbers.
    """
    output = []
    for number in numbers:
        number = remove_unnecessary_chars(number)
        number = add_country_code(number)
        if is_valid(number):
            output += [number]
    return output


def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    """Check if a contact has a correct phone number.

    Args:
        names (list[str]): A list of names with random case.
        numbers (list[str]): A list of random phone numbers.

    Returns:
        list[str]: A list of names which had correct phone numbers.
    """
    output = []
    for number in numbers:
        if is_valid(number):
            output += [names[numbers.index(number)].title()]
    return output


# 25 function test
#  Check add_country_code 1 2 3
print("add_country_code")

print(add_country_code("1234567"))  # => "+372 1234567"
print(add_country_code("+372 1234567"))  # => "+372 1234567"


# Check is_valid 4 5 6 7 8 9 10
print("is_valid")

print(is_valid("+372 1234567"))  # => True
print(is_valid("+1 1234567"))  # => True
print(is_valid("+3721234567"))  # => False
print(is_valid("+372 123456"))  # => False
print(is_valid("+372A12345*7"))  # => False


#  Check remove_unnecessary_chars 12 13 14 15 16
print("remove_unnecessary_chars")

# print(remove_unnecessary_chars("+372 *1234567a"))  # => "+372 1234567"
# print(remove_unnecessary_chars("+++37ooo2 1234+AAA567"))  # => "+372 1234567"
# print(remove_unnecessary_chars(" 123+h n456!7"))  # => "1234567"
# print(remove_unnecessary_chars("+abc 55fd"))  # => "55"
# print(remove_unnecessary_chars("+abc   ++ "))  # => ""
# print(remove_unnecessary_chars("+372 adbbcc%$"))  # => "372"
# print(remove_unnecessary_chars("+abc 55 5 5fd"))  # => "+55 55"
print(remove_unnecessary_chars("12575 +564564 + 324"))  # 1257556564324


#  Check get_last_numbers 17 18 19 20
print("get_last_numbers")

# => ["1234567", "+1 234567890"]
print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 2))
print(get_last_numbers(["+372 1234567"], 3))  # => ["+372 1234567"]
print(get_last_numbers(
    ["+372 1234567", "1234567", "+1 234567890"], 0))  # => []


#  Check get_first_correct_number 21 22 23 24 26
print("get_first_correct_number")

print(get_first_correct_number(["Alice Smith", "Bob Brown", "Carol White"], [
      "+372 1234567", "555-1234", "+1 234567890"], "Alice Smith"))  # => "+372 1234567"
print(get_first_correct_number(["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], [
      "555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith"))  # => "+1 234567890"
print(get_first_correct_number(["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], [
      "555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "Alice Smith"))  # => None


#  Check correct_numbers 27 31 32
print("correct_numbers")

# => ["+372 1234567", "+111 23456789"]
print(correct_numbers(["+372 12345", "1234567", "+111 23456789", "456"]))
# => ["+372 1234567", "+1 234567890", "+372 5551234", "+372 51234567", "+372 59876543"]
print(correct_numbers(["1234567", "+1 234567890",
      "5551234", "+372 51234567", "+372 59876543"]))
# => ["+44 1234567", "+372 5551234"]
print(correct_numbers(["+372 123456", "+44 1234567AAA", "555-1234"]))
print(correct_numbers(["555-1234", "123", "AAAAA"]))  # => ["+372 5551234"]
print(correct_numbers(["5234", "123", "A8AA", "+1 12345"]))  # => []


#  Check get_names_of_contacts_with_correct_numbers
print("get_names_of_contacts_with_correct_numbers")

print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "Carol White"], [
      "+372 1234567", "555-1234", "+1 234567890"]))  # => ["Alice Smith", "Carol White"]
print(get_names_of_contacts_with_correct_numbers(["Alice Smith", "Bob Brown", "Carol White"], [
      "+372 123456", "555-1234", "*1 234567890"]))  # => []
print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "alice smith"], [
      "+372 1234567", "555-1234", "+1 234567890"]))  # => ["Alice Smith", "Alice Smith"]

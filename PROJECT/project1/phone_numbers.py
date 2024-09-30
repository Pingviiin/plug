def add_country_code(number: str) -> str:
    if number[0] == "+":
        return number
    else:
        return "+372 " + number


def is_valid(number: str) -> str:
    pass


def remove_unnecessary_chars(number: str) -> str:
    pass


def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    pass


def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    pass
                    

def correct_numbers(numbers: list[str]) -> list[str]:
    pass


def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    pass

#  Check add_country_code
print("add_country_code")

print(add_country_code("1234567")) # => "+372 1234567"
print(add_country_code("+372 1234567")) # => "+372 1234567"


# Check is_valid
print("is_valid")

print(is_valid("+372 1234567")) # => True
print(is_valid("+1 1234567")) # => True
print(is_valid("+3721234567")) # => False
print(is_valid("+372 123456")) # => False
print(is_valid("+372A12345*7")) # => False


#  Check remove_unnecessary_chars
print("remove_unnecessary_chars")

print(remove_unnecessary_chars("+372 *1234567a")) # => "+372 1234567"
print(remove_unnecessary_chars("+++37ooo2 1234+AAA567")) # => "+372 1234567"
print(remove_unnecessary_chars(" 123+h n456!7")) # => "1234567"
print(remove_unnecessary_chars("+abc 55fd")) # => "55"
print(remove_unnecessary_chars("+abc   ++ ")) # => ""
print(remove_unnecessary_chars("+372 adbbcc%$")) # => "372""
print(remove_unnecessary_chars("67865797689564536"))


#  Check get_last_numbers
print("get_last_numbers")

print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 2)) # => ["1234567", "+1 234567890"]
print(get_last_numbers(["+372 1234567"], 3)) # => ["+372 1234567"]
print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 0)) # => []


#  Check get_first_correct_number
print("get_first_correct_number")

print(get_first_correct_number(["Alice Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"], "Alice Smith")) #=> "+372 1234567"
print(get_first_correct_number(["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith"))# => "+1 234567890"
print(get_first_correct_number(["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "Alice Smith")) #=> None


#  Check correct_numbers
print("correct_numbers")

print(correct_numbers(["+372 12345", "1234567", "+111 23456789", "456"])) #=> ["+372 1234567", "+111 23456789"]
print(correct_numbers(["1234567", "+1 234567890", "5551234", "+372 51234567", "+372 59876543"])) #=> ["+372 1234567", "+1 234567890", "+372 5551234", "+372 51234567", "+372 59876543"]
print(correct_numbers(["+372 123456", "+44 1234567AAA", "555-1234"])) #=> ["+44 1234567", "+372 5551234"]
print(correct_numbers(["555-1234", "123", "AAAAA"])) #=> ["+372 5551234"]
print(correct_numbers(["5234", "123", "A8AA", "+1 12345"])) #=> []


#  Check get_names_of_contacts_with_correct_numbers
print("get_names_of_contacts_with_correct_numbers")

print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"])) # => ["Alice Smith", "Carol White"]
print(get_names_of_contacts_with_correct_numbers(["Alice Smith", "Bob Brown", "Carol White"], ["+372 123456", "555-1234", "*1 234567890"])) # => []
print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "alice smith"], ["+372 1234567", "555-1234", "+1 234567890"])) # => ["Alice Smith", "Alice Smith"]

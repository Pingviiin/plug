
def add_country_code(number: str) -> str:
    if number.startswith("+"):
        return number
    else:
        return "+372 " + number
    


def is_valid(number: str) -> str:
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
    output = ""
    for i in range(len(number)):
        if number[i].isdigit():
            output += number[i]
        if number[i] == "+":
            if number[i + 1].isdigit() and any(n.isdigit() for n in number[number.index(" "):]):
                output += number[i]
        if number[i] == " ":
            if any(n.isdigit() for n in number[number.index(" ")::-1]) and any(n.isdigit() for n in number[number.index(" "):]):
                output += number[i]
    return output



    """
    num = number.rsplit(" ", 1)
    
    cc = num[0]
    if len(num) > 1:
        num = num[1]


    cc = list(cc)
    cc = filter(lambda x: x.isdigit(), cc)
    cc = "".join(cc)
    
    num = list(num)
    num = filter(lambda x: x.isdigit(), num)
    num = "".join(num)


    if num == cc:
        return num
    
    if num == "":
        return cc
    
    if cc == "":
        return num
    
    if number[0] == "+":
        return f"+{cc} {num}"
    
    return cc + num
    """
    
    
def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    if n > len(numbers):
        return numbers
    if n <= 0:
        return []
    return numbers[-n::]




def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    for i in range(len(names)):
        if name.lower() == names[i].lower():
            if is_valid(numbers[i]):
                return numbers[i]

def correct_numbers(numbers: list[str]) -> list[str]:
    output = []
    for i in numbers:
        i = add_country_code(i)
        i = remove_unnecessary_chars(i)
        if is_valid(i):
            output += [i]
    return output


def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    output = []
    for number in numbers:
        if is_valid(number):
            output += [names[numbers.index(number)].title()]
    return output

# 25 function test
#  Check add_country_code 1 2 3
print("add_country_code")

print(add_country_code("1234567")) # => "+372 1234567"
print(add_country_code("+372 1234567")) # => "+372 1234567"


# Check is_valid 4 5 6 7 8 9 10
print("is_valid")

print(is_valid("+372 1234567")) # => True
print(is_valid("+1 1234567")) # => True
print(is_valid("+3721234567")) # => False
print(is_valid("+372 123456")) # => False
print(is_valid("+372A12345*7")) # => False


#  Check remove_unnecessary_chars 12 13 15 16 - 14 on puudu
print("remove_unnecessary_chars")

print(remove_unnecessary_chars("+372 *1234567a")) # => "+372 1234567"
print(remove_unnecessary_chars("+++37ooo2 1234+AAA567")) # => "+372 1234567"
print(remove_unnecessary_chars(" 123+h n456!7")) # => "1234567"
print(remove_unnecessary_chars("+abc 55fd")) # => "55"
print(remove_unnecessary_chars("+abc   ++ ")) # => ""
print(remove_unnecessary_chars("+372 adbbcc%$")) # => "372"
print(remove_unnecessary_chars("+112345 67890")) # => "11234567890"


#  Check get_last_numbers 17 18 19 20
print("get_last_numbers")

print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 2)) # => ["1234567", "+1 234567890"]
print(get_last_numbers(["+372 1234567"], 3)) # => ["+372 1234567"]
print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 0)) # => []


#  Check get_first_correct_number 21 22 23 24 26
print("get_first_correct_number")

print(get_first_correct_number(["Alice Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"], "Alice Smith")) #=> "+372 1234567"
print(get_first_correct_number(["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith"))# => "+1 234567890"
print(get_first_correct_number(["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "Alice Smith")) #=> None


#  Check correct_numbers 27 31 32
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

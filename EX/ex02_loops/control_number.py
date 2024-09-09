"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """
    Given encrypted string that has a control number in the end of it, return True if correct, else False.

    Calculating the correct control number:
    1. Start the calculation from 0.
    2. Add 1 for every lowercase occurrence.
    3. Add 2 for every uppercase occurrence.
    4. Add 5 for any of the following symbol occurrences: "?!@#".
    Other symbols/letters/digits don't affect the result.

    NB! If for example the number you come up with is 25, you only have to check the last two digits of the string.
    e.g. control_number("?!?!#4525") -> True, because it ends with 25.

    :param encrypted_string: encrypted string
    :return: validation
    """

    encrypted_string_lower = len(list(filter(lambda x: x.islower(), encrypted_string)))
    encrypted_string_upper = len(list(filter(lambda x: x.isupper(), encrypted_string)))


    encrypted_string_symbols = 0
    symbols = ["?", "!", "@", "#"]

    for i in encrypted_string:
        if i in symbols:
            encrypted_string_symbols += 1

    control_number = 0
    control_number = (encrypted_string_lower * 1) + (encrypted_string_upper * 2) + (encrypted_string_symbols * 5)
    

    # Find the number at the end of the string
    string_number = ""
    for i in encrypted_string[::-1]:
        if len(string_number) >= len(str(control_number)):
            break
        elif i.isdigit():
            string_number += i
        elif i.isdigit() != True:
            break
    
    # Flip it like a burger
    string_number = string_number[::-1]

    # Check if the number at the end of the string is the same as the control number
    if int(string_number) == control_number:
        return True
    else:
        return False
    

if __name__ == '__main__':
    print(control_number("asdoijODFafiaf#???___!!asidADOFJ...&paskpo#!?!387")) # True
    print(control_number("mE0W5"))  # True
    print(control_number("SomeControlNR?20"))  # False
    print(control_number("False?Nr9"))  # False
    print(control_number("#Hello?!?26"))  # True
    print(control_number("3423982340000000.....///....0"))  # True
    print(control_number("#Shift6"))  # False
    

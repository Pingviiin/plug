"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    # Find the sum of uppercase and lowercase respectively letters in the given string
    uppercase_letter_sum = len(list(filter(lambda x: x.isupper(), letter)))
    lowercase_letter_sum = len(list(filter(lambda x: x.islower(), letter)))

    # Find the sum of digits in the given string
    digits = list(filter(lambda x: x.isdigit(), letter))
    digits_sum = sum(map(int, digits))

    # Match all the conditions given
    return uppercase_letter_sum > lowercase_letter_sum and digits_sum <= uppercase_letter_sum and digits_sum >= lowercase_letter_sum


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True

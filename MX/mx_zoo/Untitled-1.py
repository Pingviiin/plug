"""Capitalize letters in text."""


def capitalize_letters(text: str) -> str:
    """
    If a letter is present in given string in both lowercase and uppercase, capitalize all occurrences of the letter.

    Examples:
    capitalize_letters("") -> ""
    capitalize_letters("abbA") -> "AbbA"
    capitalize_letters("abBa") -> "aBBa"
    capitalize_letters("AbBa") -> "ABBA"
    capitalize_letters("AbbA") -> "AbbA
    capitalize_letters("abba") -> "abba"
    capitalize_letters("ABBA") -> "ABBA"

    :param text: given text
    :return: capitalized text
    """
    # Write your code here
    uppercase = []
    for i in text:
        if i.isupper():
            uppercase.append(i)
    
    for l in uppercase:
        text = text.replace(l.lower(), l.upper())
             
    return text

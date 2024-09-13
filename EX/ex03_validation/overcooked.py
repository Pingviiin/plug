"""
See on väga kaua ahjus küpsenud.

old_pass = "eva1970"  # == "0791ave"
new_pass = "0791ave"
matching_value = 0

for i in reversed(old_pass):
    for x in new_pass:
        if x == i:
            matching_value += 1
    else:
        matching_value -= 1

if matching_value == 0:
    print(True)
else:
    print(len(old_pass) / matching_value < 0.5)


def is_name_in_password(password: str, name: str) -> bool:
    #  Convert the string into a letter frequency dictionary.
    new_pass_characters = {}
    for i in new_pass:
        if i in new_pass_characters:
            new_pass_characters[i] += 1
        else:
            new_pass_characters[i] = 1

    old_pass_characters = {}
    for i in old_pass:
        if i in old_pass_characters:
            old_pass_characters[i] += 1
        else:
            old_pass_characters[i] = 1

    #  Check if the old password and the new password have the same character in the dict.
    #  If they do, return the amount of matching characters. At the end calculate the percentage of matching characters.
    match_value = 0

    for i in old_pass_characters:
        if i in new_pass_characters.keys() and i in old_pass_characters.keys():
            if new_pass_characters.get(i) == old_pass_characters.get(i):
                match_value += new_pass_characters.get(i)
            elif new_pass_characters.get(i) < old_pass_characters.get(i):
                match_value += new_pass_characters.get(i)
            else:
                match_value += old_pass_characters.get(i)

    if match_value == len(new_pass):
        return False
    return match_value / len(new_pass) <= 0.5

    #  Ma siiralt loodan, et selle jaoks ei ole mingit funktsiooni juba sisse ehitatud
    splice_length = math.ceil(len(new_pass) / 2)

    spliced_new_pass = []
    for i in range(0, len(new_pass), splice_length):
        spliced_new_pass += [new_pass[i:i+splice_length]]

    spliced_reversed_new_pass = []
    for i in range(0, len(reversed_new_pass), splice_length):
        spliced_reversed_new_pass += [reversed_new_pass[i:i+splice_length]]

    match_value = 0
    for i in range(0, len(new_pass) // splice_length):
        if spliced_new_pass[i] in old_pass:
            match_value += 1
        elif spliced_reversed_new_pass[i] in old_pass:
            match_value += 1
        if match_value >= (len(new_pass) / splice_length) / 2:
            return False
    else:
        return True
"""

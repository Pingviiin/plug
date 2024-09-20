"""Operations with data structures."""


def rotate_list(lst, x) -> list:
    """
    Rotate a list by x positions to the right.

    If x is bigger than or equal to list's length, return a reversed list.

    :param lst: The list to rotate.
    :param x: The number of positions to rotate.
    :return: The rotated list.
    """
    if len(lst) <= x:
        return lst[::-1]
    for i in range(0, x):
        element = lst[-1]
        lst.pop(-1)
        lst.insert(0, element)

    return lst


def filter_dict(dictionary, threshold) -> list:
    """
    Return a list of values for which the key was above the threshold.

    :param dictionary: The dictionary to filter.
    :param threshold: The threshold value.
    :return: A list of values with keys above the threshold.
    """
    return [dictionary[key] for key in dictionary if key > threshold]


def merge_dicts(dict1, dict2) -> dict:
    """
    Merge two dictionaries, with values from dict2 overwriting those from dict1 for matching keys.

    :param dict1: The first dictionary.
    :param dict2: The second dictionary.
    :return: The merged dictionary.
    """
    dict1.update(dict2)
    return dict1


def indexed_list(lst) -> dict:
    """
    Convert the SORTED list of strings to a dict with indexes as keys and strings as values.

    Before indexing, sort the list so that the shortest string is first and the longest string is last. If
    two strings have the same length, sort them in alphabetical order.

    :param lst: list to use for dict values
    :return: dict with indexes as keys and list elements as values
    """
    lst.sort(reverse=False, key=lambda x: len(x))
    return {lst.index(key): key for key in lst}


def set_operations(set1, set2, result_dict) -> dict:
    """
    Return a dictionary with set operations results.

    The dictionary contains the following keys:
    - 'union': the union of set1 and set2
    - 'intersection': the intersection of set1 and set2
    - 'difference': the difference of set1 and set2
    - 'symmetric_difference': the symmetric difference of set1 and set2
    All the values are empty sets and should be filled with the corresponding set operation results.

    :param set1: The first set.
    :param set2: The second set.
    :param result_dict: The dictionary to store the results.
    :return: A dictionary with set operations results.
    """
    output = {}
    output["union"] = set1 | set2
    output["intersection"] = set1 & set2
    output["difference"] = set1 - set2
    output["symmetric_difference"] = set1 ^ set2
    return output


def sort_list_of_tuples(lst) -> list:
    """
    Sort a list of tuples by the second element of each tuple in ascending order.

    If two tuples have the same second element, sort them by the first element in ascending order.
    The tuples inside the list contain only integers, no need to check for other types.

    :param lst: The list of tuples to sort.
    :return: The sorted list of tuples.
    """
    lst.sort(key=lambda i: i[0])
    lst.sort(key=lambda i: i[1])
    return lst


def create_dict_from_tuples_and_lists(tuples, lists) -> dict:
    """
    Create a dictionary from the given tuples and lists.

    The dictionary should contain the tuples as keys and the lists as values.
    If there is a mismatch in the number of tuples and lists, return an empty dictionary.

    :param tuples: The list of tuples to use as keys.
    :param lists: The list of lists to use as values.
    :return: The dictionary created from the tuples and lists.
    """
    return {tuples[i]: lists[i] for i in range(len(tuples)) if len(tuples) == len(lists)}


def extract_information_from_string(string) -> dict:
    """
    Extract information from the given string.

    The string contains information about a person in the following format:
    "Name: John, Age: 30, City: New York, Job: Engineer"
    The keys are always the same, but the values change.
    Return a dictionary with the keys as the dictionary keys and the values as the dictionary values.

    :param string: The string containing the information.
    :return: A dictionary with the extracted information.
    """
    string = string.replace(": ", ", ")
    giga_list = string.split(", ")
    return {giga_list[e]: giga_list[e + 1] for e in range(0, len(giga_list) - 1, 2)}


def remove_duplicates(lst) -> list:
    """
    Remove duplicates from the given list.

    The order of the elements should be preserved.

    :param lst: The list to remove duplicates from.
    :return: The list with duplicates removed.
    """
    output = []
    [output.append(el) for el in lst if el not in output]
    return output


def sort_dict_values(dictionary) -> dict:
    """
    Sort the value lists of the given dictionary in ascending order.

    The keys remain the same. The values are lists of integers which need to be sorted from smallest to largest.

    :param dictionary: The dictionary to sort.
    :return: The dictionary with sorted values.
    """
    for key in dictionary:
        dictionary[key].sort()
    return dictionary


def tuple_of_tuples(lst) -> tuple:
    """
    Create a tuple of tuples from the given list.

    Each tuple should contain one element from the list.

    :param lst: The list to convert to a tuple of tuples.
    :return: The tuple of tuples.
    """
    tuple_list = [(i,) for i in lst]
    return tuple(tuple_list)


def element_exists(lst1, dict1, set1, tuple1, element) -> bool:
    """
    Check if the element exists in every data structure.

    The element can be in both the key or the value of the dictionary. "3" and 3 are not the same.

    :param lst1: The list to check.
    :param dict1: The dictionary to check.
    :param set1: The set to check.
    :param tuple1: The tuple to check.
    :param element: T.
    :return: True if the element exists in all data structures, False otherwise.
    """
    return element in lst1 and dict1 and set1 and tuple1


def min_max(lst1, dict1, set1, tuple1) -> tuple:
    """
    Return the minimum and maximum values from the data structures.

    The minimum and maximum values should be returned as a tuple in the following order:
    - list: minimum, maximum
    - dictionary: minimum key, maximum key, minimum value, maximum value
    - set: minimum, maximum
    - tuple: minimum, maximum
    All values are integers and all data structures contain at least two elements.

    :param lst1: The list to check.
    :param dict1: The dictionary to check.
    :param set1: The set to check.
    :param tuple1: The tuple to check.
    :return: A tuple with the minimum and maximum values as tuples.
    """
    return ((min(lst1), max(lst1)), (min(dict1.keys()), max(dict1.keys()), min(dict1.values()), max(dict1.values())), (min(set1), max(set1)), (min(tuple1), max(tuple1)))


def unique_primes(numbers) -> set:
    """
    Identify unique prime numbers from a list.

    Number is prime if it is greater than 1 and has no divisors other than 1 and itself. Unique means that there is only
    one occurrence of the prime number in the result even if it occurs multiple times in the input.

    :param numbers: A list of integers.
    :return: A set of unique prime numbers from the list.
    """
    output = set()
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                output.add(number)
        else:
            break
    return output


def unique_word_lengths(text):
    """
    Return unique word lengths from the given text.

    The text contains only letters and spaces. Words are separated by spaces. The word length is unique if there
    is only one word of that length.

    :param: text (str): The input string to analyze.
    :return: A set containing unique word lengths.
    """
    output = set()
    lst = text.split(" ")
    len_list = [len(el) for el in lst]

    for i in len_list:
        if len_list.count(i) <= 1:
            output.add(i)

    return output


if __name__ == "__main__":
    # rotate_list
    rotated = rotate_list([1, 2, 3, 4, 5], 2)
    print("rotate_list:", rotated)
    print("Answer is correct:", rotated == [4, 5, 1, 2, 3])

    # filter_dict
    filtered = filter_dict({1: 'a', 2: 'b', 3: 'c'}, 1)
    print("filter_dict:", filtered)
    print("Answer is correct:", filtered == ['b', 'c'])

    # merge_dicts
    merged = merge_dicts({1: 'a', 2: 'b'}, {2: 'c', 3: 'd'})
    print("merge_dicts:", merged)
    print("Answer is correct:", merged == {1: 'a', 2: 'c', 3: 'd'})

    # indexed_list
    indexed = indexed_list(["banana", "apple", "cherry", "date", "pear"])
    print("indexed_list:", indexed)
    print("Answer is correct:", indexed == {
          0: 'date', 1: "pear", 2: 'apple', 3: 'banana', 4: 'cherry'})

    # set_operations
    set_result = {'union': set(), 'intersection': set(
    ), 'difference': set(), 'symmetric_difference': set()}
    set_ops = set_operations({1, 2, 3}, {2, 3, 4}, set_result)
    print("set_operations:", set_ops)
    print("Answer is correct:", set_ops == {'union': {1, 2, 3, 4}, 'intersection': {2, 3},
                                            'difference': {1}, 'symmetric_difference': {1, 4}})

    # sort_list_of_tuples
    sorted_tuples = sort_list_of_tuples([(1, 2), (3, 1), (1, 1)])
    print("sort_list_of_tuples:", sorted_tuples)
    print("Answer is correct:", sorted_tuples == [(1, 1), (3, 1), (1, 2)])

    # create_dict_from_tuples_and_lists
    created_dict = create_dict_from_tuples_and_lists(
        [(1, 2), (3, 4)], [[5, 6], [7, 8]])
    print("create_dict_from_tuples_and_lists:", created_dict)
    print("Answer is correct:", created_dict == {(1, 2): [5, 6], (3, 4): [7, 8]})

    # extract_information_from_string
    extracted_info = extract_information_from_string(
        "Name: John, Age: 30, City: New York, Job: Engineer")
    print("extract_information_from_string:", extracted_info)
    print("Answer is correct:", extracted_info == {'Name': 'John', 'Age': '30',
                                                   'City': 'New York', 'Job': 'Engineer'})

    # remove_duplicates
    no_duplicates = remove_duplicates([1, 2, 3, 1, 2, 4])
    print("remove_duplicates:", no_duplicates)
    print("Answer is correct:", no_duplicates == [1, 2, 3, 4])

    # sort_dict_values
    sorted_dict = sort_dict_values({1: [3, 1, 2], 2: [9, 7, 8]})
    print("sort_dict_values:", sorted_dict)
    print("Answer is correct:", sorted_dict == {1: [1, 2, 3], 2: [7, 8, 9]})

    # tuple_of_tuple
    tuples = tuple_of_tuples([1, 2, 3])
    print("tuple_of_tuples:", tuples)
    print("Answer is correct:", tuples == ((1,), (2,), (3,)))

    # element_exists
    exists = element_exists([1, 2, 3], {1: 'a', 2: 'b'}, {1, 2}, (1, 2, 3), 2)
    print("element_exists:", exists)
    print("Answer is correct:", exists)

    # min_max
    minmax = min_max([1, 2, 3], {1: 'a', 2: 'b'}, {3, 1}, (2, 4))
    print("min_max:", minmax)
    print("Answer is correct:", minmax == (
        (1, 3), (1, 2, 'a', 'b'), (1, 3), (2, 4)))

    # unique_primes
    primes = unique_primes([2, 3, 4, 5, 6, 7, 7, 8, 9, 2, 101])
    print("unique_primes:", primes)
    print("Answer is correct:", primes == {2, 3, 5, 7, 101})

    # unique_word_lengths
    word_lengths = unique_word_lengths("hello world nice job nice weather")
    print("unique_word_lengths:", word_lengths)
    print("Answer is correct:", word_lengths == {3, 7})

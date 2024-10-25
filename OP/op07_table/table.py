"""Create table from the given string."""
import re

def create_table_string(text: str) -> str:
    """
    Create table string from the given logs.

    There are a total of five categories you need to find the items for.
    Here are the rules for finding them:

    1. Time
    - Hour can be one or two characters long (1, 01, and 11)
    - Minute can be one or two characters long (2, 02, 22)
    - UTC offset ranges from -12 to 12
    - Times in the text are formatted in 24-hour time format (https://en.wikipedia.org/wiki/24-hour_clock)
    - Minimum time is 00:00 (0:00 and 0,00 and 00-0 are also valid)
    - Maximum time is 23:59
    - Hour and minute can be separated by any non-numeric character (01:11, 1.2, 6;5 and 1a4 are valid while 12345 is not)
    2. Username starts after "usr:" and contains letters, numbers and underscores ("_")
    3. Error code is a non-negative number up to 3 digits and comes after a case-insensitive form of "error "
    4. IPv4 address is good enough if it's a group of four 1- to 3-digit numbers separated by dots
    5. Endpoint starts with a slash ("/") and contains letters, numbers and "&/=?-_%"

    Each table row consists of a category name and items belonging to that category.
    Categories are named and ordered as follows: "time", "user", "error", "ipv4" and "endpoint".

    The category name and its items are separated by a vertical bar ("|").
    The length between the category name and separator is one whitespace (" ") for the longest category name in the table.
    The length between the separator and items is one whitespace.
    Items for each category are unique and are separated by a comma and a whitespace (", ") and must be sorted in ascending order.
    Times in the table are formatted in 12-hour time format (https://en.wikipedia.org/wiki/12-hour_clock), like "1:12 PM"
    and "12:00 AM".
    Times in the table should be displayed in UTC(https://et.wikipedia.org/wiki/UTC) time.
    If no items were found, return an empty string.
    """
    
    "pikima_kategooria_nimi + üks_tühik + eraldaja + üks_tühik + kategooria_logi_andmed"
    time = format_time(get_times(text))
    user = get_usernames(text)
    error = get_errors(text)
    ipv4 = get_addresses(text)
    endpoint = get_endpoints(text)
    return f"{time}\n{user}\n{error}\n{ipv4}\n{endpoint}"


def get_times(text: str) -> list[tuple[int, int, int]]:
    """
    Get times from text using the time pattern. No need to sort here.

    The result should be a list of tuples containing the time that's not normalized and UTC offset: (hours, minutes, utc_offset) in that order.

    :param text: text to search for the times
    :return: list of tuples containing the time and offset
    """
    pattern = r"\[(\d{1,2})\D(\d{1,2}) UTC([+-])(\d)"
    match = re.findall(pattern, text)
    
    output = []
    if match != []:
        for m in match:
            hours = int(m[0])
            minutes = int(m[1])
            
            utc_sign = m[2]
            utc_time = int(m[3])
            
            if utc_sign == "-":
                utc_time = -utc_time
            
            output += [(hours, minutes, utc_time)]

    return output
    

def format_time(time_list: list) -> list:
    """Format time data to 12-hour format."""

    if time_list == []:
        return []

    output = []
    for tup in time_list:
        hours = tup[0]
        minutes = tup[1]
        utc_time = tup[2]

        hours = (hours + -utc_time) % 24

        if hours == 0:
            meridiem = "AM"
            hours = 12
        elif hours < 12:
            meridiem = "AM"
        elif hours == 12:
            meridiem = "PM"
        else:
            meridiem = "PM"
            hours = hours - 12

        output += [f"{hours}:{minutes:02d} {meridiem}"]
    
    return output



def get_usernames(text: str) -> list[str]:
    """Get usernames from text. No need to sort here."""
    pattern = r"usr:([\w]+)"
    return re.findall(pattern, text)


def get_errors(text: str) -> list[int]:
    """Get errors from text. No need to sort here."""
    pattern = r"error\s([\d]{1,3})"
    return re.findall(pattern, text, re.IGNORECASE)


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text. No need to sort here."""
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.findall(pattern, text)


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text. No need to sort here."""
    pattern = r"/([\w&/=?-_%]+)"
    return re.findall(pattern, text)


if __name__ == '__main__':
    logs = """
[-1b35 UTC-4] errOR 741
[24a48 UTC+0] 776.330.579.818
[02:53 UTC+5] usr:96NC9yqb /aA?Y4pK
[5b05 UTC+5] ERrOr 700 268.495.856.225
[24-09 UTC+10] usr:uJV5sf82_ eRrOR 844 715.545.485.989
[04=54 UTC+3] eRROR 452
[11=57 UTC-6] 15.822.272.473 error 9
[15=53 UTC+7] /NBYFaC0 468.793.214.681
[23-7 UTC+12] /1slr8I
[07.46 UTC+4] usr:B3HIyLm 119.892.677.533

[0:60 UTC+0] bad
[0?0 UTC+0] ok
[0.0 UTC+0] also ok
            """
    #print(get_endpoints(f'/cfepechz /api/orders')) # -> ['/cfepechz', '/api/orders']
    #print(get_times("[-1b35 UTC+0")) # -> []
    #print(get_times("[10:53 UTC+3]")) # -> [(10, 53, 3)]
    #print(get_times("[1:43 UTC+0]")) # -> [(1, 43, 0)]
    #print(get_times("[14A3 UTC-4] [14:3 UTC-4]"))# -> [(14, 3, -4), (14, 3, -4)]
    #print("")
    #print(get_times(logs))
    print(create_table_string(logs))
#time     | 12:00 AM, 12:05 AM, 1:54 AM, 3:46 AM, 8:53 AM, 11:07 AM, 5:57 PM, 9:53 PM
#user     | 96NC9yqb, B3HIyLm, uJV5sf82_
#error    | 9, 452, 700, 741, 844
#ipv4     | 119.892.677.533, 15.822.272.473, 268.495.856.225, 468.793.214.681, 715.545.485.989, 776.330.579.818
#endpoint | /1slr8I, /NBYFaC0, /aA?Y4pK
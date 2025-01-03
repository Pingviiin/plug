"""Some cool pyramids."""


def create_simple_pyramid_left(height: int, pyramid_row: int = 1) -> str:
    """
    Create simple pyramid on the left side.

    *
    **
    ***
    ****

    Use recursion!

    :param height: Pyramid height.
    :return: Pyramid.
    """
    if pyramid_row > height:
        return ""

    return (pyramid_row * "*") + "\n" + create_simple_pyramid_left(height, pyramid_row + 1)


def create_simple_pyramid_right(height: int, current=1) -> str:
    """
    Create simple pyramid on the right side.

       *
      **
     ***
    ****

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    return "{:>{}}".format(current * "*", height) + "\n" + create_simple_pyramid_right(height, current + 1)


def create_number_pyramid_left(height: int, current=1) -> str:
    """
    Create left-aligned number pyramid.

    1
    12
    123
    1234

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    def row(n: int) -> str:
        if n == 0:
            return ""
        return row(n - 1) + str(n)

    current_row = row(current)

    return current_row + "\n" + create_number_pyramid_left(height, current + 1)


def create_number_pyramid_right(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid.

        1
       21
      321
     4321

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = ' ' * (height - current)

    numbers = ''.join(str(i) for i in range(current, 0, -1))

    current_layer = f"{spaces}{numbers}"

    return f"{current_layer}\n" + create_number_pyramid_right(height, current + 1)


def create_number_pyramid_left_down(height: int, current=0) -> str:
    """
    Create left-aligned number pyramid upside-down.

    4321
    321
    21
    1

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if height == 0:
        return ""

    def row(n: int) -> str:
        if n == 0:
            return ""
        return f"{n}{row(n - 1)}"

    current_row = row(height)
    rem_pyramid = create_number_pyramid_left_down(height - 1, current + 1)

    return current_row + "\n" + rem_pyramid if rem_pyramid else current_row


def create_number_pyramid_right_down(height: int, current=1) -> str:
    """
    Create right-aligned number pyramid upside-down.

    1234
     123
      12
       1

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if height == 0:
        return ""

    def row(n: int) -> str:
        if n == 0:
            return ""
        return row(n - 1) + str(n)

    spaces = " " * (current - 1)
    current_layer = row(height)
    rem_pyramid = create_number_pyramid_right_down(height - 1, current + 1)

    return f"{spaces}{current_layer}\n{rem_pyramid}" if rem_pyramid else f"{spaces}{current_layer}"


def create_regular_pyramid(height: int, current=1) -> str:
    """
    Create regular pyramid.

       *
      ***
     *****
    *******

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = ' ' * (height - current)
    stars = '*' * (2 * current - 1)

    current_layer = f"{spaces}{stars}"

    return f"{current_layer}\n" + create_regular_pyramid(height, current + 1)


def create_regular_pyramid_upside_down(height: int, current=1) -> str:
    """
    Create regular pyramid upside down.

    *******
     *****
      ***
       *

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = ' ' * (current - 1)
    stars = '*' * (2 * (height - current + 1) - 1)

    current_layer = f"{spaces}{stars}"

    return f"{current_layer}\n" + create_regular_pyramid_upside_down(height, current + 1)


def create_diamond(height: int, current=1) -> str:
    """
    Create diamond using recursion.

       *
      ***
     *****
    *******
    *******
     *****
      ***
       *

    :param height: Height of half of the diamond.
    :param current: Keeping track of current layer.
    :return: Diamond as a string.
    """
    if current > height:
        return create_diamond_bottom(height, current - 1)

    spaces = ' ' * (height - current)
    stars = '*' * (2 * current - 1)

    current_layer = f"{spaces}{stars}"

    return f"{current_layer}\n" + create_diamond(height, current + 1)


def create_diamond_bottom(height: int, current) -> str:
    """
    Create the bottom half of the diamond using recursion.

    :param height: Height of half of the diamond.
    :param current: Current layer for the bottom part of the diamond.
    :return: Bottom part of the diamond as a string.
    """
    if current == 0:
        return ""

    spaces = ' ' * (height - current)
    stars = '*' * (2 * current - 1)

    current_layer = f"{spaces}{stars}"

    return f"{current_layer}\n" + create_diamond_bottom(height, current - 1)


def create_empty_pyramid(height: int, current=1) -> str:
    """
    Create empty pyramid.

       *
      * *
     *   *
    *******

    Use recursion!

    :param height: Pyramid height.
    :param current: Keeping track of current layer.
    :return: Pyramid.
    """
    if current > height:
        return ""

    spaces = ' ' * (height - current)

    if current == 1:
        stars = '*'
    elif current == height:
        stars = '*' * (2 * current - 1)
    else:
        inner_spaces = ' ' * (2 * current - 3)
        stars = f"*{inner_spaces}*"

    current_layer = f"{spaces}{stars}"

    return f"{current_layer}\n" + create_empty_pyramid(height, current + 1)


if __name__ == '__main__':
    """
    print("\ncreate_simple_pyramid_left:")
    print("expected:\n*\n**\n***\n****")
    print(f"\ngot:\n{create_simple_pyramid_left(4)}")

    print("\ncreate_simple_pyramid_right:")
    print("expected:\n   *\n  **\n ***\n****")
    print(f"\ngot:\n{create_simple_pyramid_right(4)}")

    print("\ncreate_number_pyramid_left:")
    print("expected:\n1\n12\n123\n1234")
    print(f"\ngot:\n{create_number_pyramid_left(4)}")

    print("\ncreate_number_pyramid_right:")
    print("expected:\n   1\n  21\n 321\n4321")
    print(f"\ngot:\n{create_number_pyramid_right(4)}")


    print("\ncreate_number_pyramid_right_bigger_pyramid:")
    print("expected:\n          1\n         21\n        321\n"
          "       4321\n      54321\n     654321\n    7654321\n"
          "   87654321\n  987654321\n 10987654321\n1110987654321")
    print("Or expected:\n            1\n           21\n          321\n"
          "         4321\n        54321\n       654321\n      7654321\n"
          "     87654321\n    987654321\n  10987654321\n1110987654321")
    print(f"\ngot:\n{create_number_pyramid_right(11)}")

    print("\ncreate_number_pyramid_left_down:")
    print("expected:\n4321\n321\n21\n1")
    print(f"\ngot:\n{create_number_pyramid_left_down(4)}")

    print("\ncreate_number_pyramid_right_down:")
    print("expected:\n1234\n 123\n  12\n   1")
    print(f"\ngot:\n{create_number_pyramid_right_down(4)}")
    """
    print("\ncreate_number_pyramid_right_down_bigger_pyramid:")
    print("expected:\n1234567891011\n 12345678910\n  123456789\n"
          "   12345678\n    1234567\n     123456\n      12345\n"
          "       1234\n        123\n         12\n          1")
    print("Or expected:\n1234567891011\n  12345678910\n    123456789\n"
          "     12345678\n      1234567\n       123456\n        12345\n"
          "         1234\n          123\n           12\n            1")
    print(f"\ngot:\n{create_number_pyramid_right_down(11)}")

    print("\ncreate_regular_pyramid:")
    print("expected:\n   *\n  ***\n *****\n*******")
    print(f"\ngot:\n{create_regular_pyramid(4)}")

    print("\ncreate_regular_pyramid_upside_down:")
    print("expected:\n*******\n *****\n  ***\n   *")
    print(f"\ngot:\n{create_regular_pyramid_upside_down(4)}")

    print("\ncreate_diamond:")
    print("expected:\n   *\n  ***\n *****\n*******\n*******\n *****\n  ***\n   *")
    print(f"\ngot:\n{create_diamond(4)}")

    print("\ncreate_empty_pyramid:")
    print("expected:\n   *\n  * *\n *   *\n*******")
    print(f"\ngot:\n{create_empty_pyramid(4)}")

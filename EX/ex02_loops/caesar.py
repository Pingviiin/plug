"""Caesar cipher."""


def encode(message: str, shift: int) -> str:
    """
    Encode a message using a Caesar cipher.

    Presume the message is already lowercase.
    For each letter of the message, shift it forward in the alphabet by shift amount.
    If the character isn't a letter, keep it the same.

    For example, shift = 3 then a => d, b => e, z => c (see explanation below)

    Shift:    0 1 2 3
    Alphabet:       A B C D E F G H I J
    Result:   A B C D E F G H I J

    Examples:
    1. encode('i like turtles', 6) == 'o roqk zaxzrky'
    2. encode('example', 1) == 'fybnqmf'
    3. encode('the quick brown fox jumps over the lazy dog.', 7) == 'aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

    :param message: message to be encoded
    :param shift: shift for encoding
    :return: encoded message
    """
    ciphered_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    big_alphabet = ""
    if shift != 0:
        big_alphabet = alphabet
    else:
        big_alphabet = alphabet * shift
    for letter in message:
        if letter.isalpha():
            letter_location = (alphabet.find(letter))
            letter = big_alphabet[letter_location + shift]

        ciphered_message += letter

    return ciphered_message



if __name__ == '__main__':
    #print(encode("don't change", 0))  # -> don't change
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("example", 1))  # -> fybnqmf
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.

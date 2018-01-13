from helper import convert_to_num, convert_to_alpha
import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    alphabet = string.ascii_lowercase

    digits = digits.lower()
    exponent = len(digits) - 1
    decimal_conversion = 0
    for digit in digits:
        if digit not in alphabet:
            decimal_conversion += (base ** exponent) * int(digit)
            exponent -= 1
        else:
            ordinal_val = convert_to_num(digit)
            decimal_conversion += (base ** exponent) * ordinal_val
            exponent -= 1
    return decimal_conversion

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    exponent = 0
    values = ''
    while number > 0:
        if number - (base ** exponent) < 1:
            exponent -= 1
            continue

        value = number // (base ** exponent)
        value *= (base ** exponent)
        values += str(value)
        number -= (base ** exponent) * (number // (base ** exponent))
        exponent -= 1
    return values

print(encode(1251, 4))
# def convert(digits, base1, base2):
#     """Convert given digits in base1 to digits in base2.
#     digits: str -- string representation of number (in base1)
#     base1: int -- base of given number
#     base2: int -- base to convert to
#     return: str -- string representation of number (in base2)"""
#     # Handle up to base 36 [0-9a-z]
#     assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
#     assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
#     # TODO: Convert digits from base 2 to base 16 (and vice versa)

#     exponents = get_exponents(digits)
#     decimal = get_decimal_from_binary(exponents)
    
#     return decimal
#     # TODO: Convert digits from base 10 to base 16 (and vice versa)
#     # ...
#     # TODO: Convert digits from any base to any base (2 up to 36)
#     # ...


# def main():
#     """Read command-line arguments and convert given digits between bases."""
#     import sys
#     args = sys.argv[1:]  # Ignore script file name
#     if len(args) == 3:
#         digits = args[0]
#         base1 = int(args[1])
#         base2 = int(args[2])
#         # Convert given digits between bases
#         result = convert(digits, base1, base2)
#         print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
#     else:
#         print('Usage: {} digits base1 base2'.format(sys.argv[0]))
#         print('Converts digits from base1 to base2')


# if __name__ == '__main__':
#     run_test = True
#     if run_test:
#         assert decode('0', 2) == 0
#         assert decode('1', 2) == 1
#         assert decode('10', 2) == 2
#         assert decode('11', 2) == 3
#         assert decode('100', 2) == 4
#         assert decode('101', 2) == 5
#         assert decode('110', 2) == 6
#         assert decode('111', 2) == 7
#         assert decode('1000', 2) == 8
#         assert decode('1001', 2) == 9
#         assert decode('1010', 2) == 10
#         assert decode('1011', 2) == 11
#         assert decode('1100', 2) == 12
#         assert decode('1101', 2) == 13
#         assert decode('1110', 2) == 14
#         assert decode('1111', 2) == 15
#     else:
#         main()

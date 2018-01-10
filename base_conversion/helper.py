def get_exponents(digit_str):
    '''
    digit_str: string
    function gets the exponents from a binary digit string
    returns list
    '''
    digit_length = len(digit_str) - 1
    exponents = []
    for number, digit in zip(range(digit_length, -1, -1), digit_str):
        if digit == '1':
            exponents.append(number)
    return exponents

def get_decimal_from_binary(exponents):
    return sum([2 ** expo for expo in exponents])


if __name__ == '__main__':
    digits = {
        202: '11001010',
        129: '10000001',
        250: '11111010',
        195: '11000011',
        166: '10100110',
        7: '111'
    }
    for answer, digits in digits.items():
        exponents = get_exponents(digits)
        result = sum([2 ** expo for expo in exponents])
        assert result == answer 

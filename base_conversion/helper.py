# TODO: Finish type hinting all functions
# TODO: Add docstrings
def convert_to_num(alpha_numerical):
    '''
    alpha_num: string
    function converts letter to its correct numerical value
    returns int
    '''
    return ord(letter) - 87

# def convert_to_alpha(num: int) -> str:
def convert_to_alpha(num):
    '''
    num: string
    function converts num to its correct alpha_numerical letter
    returns string
    '''
    return chr(num + 87)

# def is_dec_bigger(decimal: int, number: int):
def is_dec_bigger(decimal, number):
    return True if (decimal - number) < 1 else False

def get_encoded_val(decimal, number):
    return decimal // number

def update_decimal(decimal, number, encoded_val):
    return decimal - (number * int(encoded_val))

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
        result = sum([2 ** expo for expo in exponents])
        assert result == answer 

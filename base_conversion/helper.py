# TODO: Finish type hinting all functions
# TODO: Add docstrings
# TODO: Implement remove preceding zeros function
# TODO: Function to format nunmbers based on colon. Only for numbers of base 36 n up

def convert_to_num(alpha_numerical):
    '''
    alpha_num: string
    function converts letter to its correct numerical value
    returns int
    '''
    return ord(alpha_numerical) - 87

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

def remove_zeros(encoded_val: str):
    # get the index of the first char that is not a '0'
    index = [ind for ind, char in enumerate(encoded_val) if char != '0'][0]
    return encoded_val[index:]

if __name__ == '__main__':
    encoded_strings = ['000120B', '0001020B', '000100Ba', '00010020Ba', '000120Ba', '12b']
    answers = ['120B', '1020B', '100Ba', '10020Ba', '120Ba', '12b']
    for string, answer in zip(encoded_strings, answers):
        assert remove_zeros(string) == answer

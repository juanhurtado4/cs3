def convert_to_num(alpha_num):
    '''
    alpha_num: string
    function converts letter to its correct numerical value
    returns int
    '''
    return ord(alpha_num) - 87

def convert_to_alpha(num):
    '''
    num: string
    function converts num to its correct alpha_numerical letter
    returns string
    '''
    return chr(num + 87)

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

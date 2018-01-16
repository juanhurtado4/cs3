from palindrome_helper import *

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    '''
    text: str
    running time: o(n)
    checks if text is a palindrome
    returns boolean
    '''
    (text, left_pos, right_pos) = assign_starting_vars(text)

    while right_is_bigger(left_pos, right_pos):

        # assign multiple variables
        (left_c, right_c) = assign_chars(text, left_pos, right_pos)
            
        if chars_not_alphabet(left_c, right_c):
            left_pos = update_position('left', left_pos, left_c)
            right_pos = update_position('right', right_pos, right_c)
            continue

        if chars_dont_match(left_c, right_c): 
            return False
        else:
            left_pos += 1
            right_pos -= 1
    return True

def is_palindrome_recursive(text, left=None, right=None):
    '''
    text: str
    running time: o(n)
    checks if text is a palindrome recursively
    returns boolean
    '''
    if left == None and right == None:
        # assign multiple variables
        (text, left, right) = assign_starting_vars(text)

    if not right_is_bigger(left, right): return True

    # assign multiple variables
    (left_c, right_c) = assign_chars(text, left, right)

    if chars_not_alphabet(left_c, right_c):
            left = update_position('left', left, left_c)
            right = update_position('right', right, right_c)
            return is_palindrome_recursive(text, left, right)
    
    # not a palindrome
    if chars_dont_match(text[left], text[right]): return False

    return is_palindrome_recursive(text, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
